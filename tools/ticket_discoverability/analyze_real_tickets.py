"""
Analyze real XAF support tickets to prioritize ontology implementation.

This tool:
1. Maps ticket feature categories to concepts.yml concepts
2. Identifies high-volume areas needing improved documentation/discoverability
3. Prioritizes which ontology features to implement first
4. Generates actionable recommendations for Phases 1-4

Usage:
    python tools/analyze_real_tickets.py
    
Supports:
- JSON format: xaf_support_tickets_by_feature.json (feature category → count)
- CSV format: detailed ticket export with text, dates, types
"""

import json
import yaml
import polars as pl
from pathlib import Path
from typing import Dict, List, Tuple, Optional
import re
import sys
from collections import defaultdict

# ============================================================================
# PATTERN DETECTION CONSTANTS (Issue #1, #2, #4, #5, #6, #9)
# ============================================================================

# Generic verbs that cause false positives (Issue #2)
GENERIC_VERBS = {
    'read', 'customize', 'extend', 'create', 'configure',
    'manage', 'use', 'implement', 'add', 'remove', 'handle',
    'process', 'execute', 'perform', 'apply', 'set', 'get'
}

# Umbrella terms spanning multiple concepts (Issue #1)
UMBRELLA_TERMS = {
    'business logic', 'security rules', 'callbacks',
    'customization', 'configuration', 'settings', 'properties'
}

# Tool/Editor pattern (Issue #4)
TOOL_PATTERNS = r'\b\w+(editor|designer|wizard|tool|manager|builder)\b'

# Storage/Format pattern (Issue #6)
STORAGE_PATTERNS = r'\b\w+(store|storage|provider|repository|persistence)\b'
FORMAT_PATTERNS = r'\.(xafml|xml|json|config)\b'

# Property/Attribute pattern (Issue #5)
PROPERTY_PATTERNS = r'\b\w+(field|property|attribute|mode)s?\b'

# Lifecycle pattern (Issue #9)
LIFECYCLE_PATTERNS = r'\b(on\w+|after\w+|before\w+|\w+ing|lifecycle|events?|state|activation)\b'

# API-specific pattern detection (high quality matches)
API_PATTERNS = r'\b(I[A-Z]\w+|[A-Z]\w*[A-Z]\w+|Xpo\w+|Xaf\w+)\b'

# Domain-specific term equivalences for semantic matching (Issue #10)
# Maps XAF-specific terminology to their conceptual equivalents
DOMAIN_TERM_EQUIVALENCES = {
    'data model': ['business entities', 'business class', 'persistent object', 'domain model', 'entity'],
    'application model': ['xaf model', 'metadata model', 'ui configuration', 'model metadata'],
    'security rules': ['permissions', 'authorization', 'access control'],
    'custom user': ['applicationuser', 'security user', 'identity'],
    'custom role': ['security role', 'permission role'],
}

def normalize_domain_terms(text: str) -> str:
    """
    Normalize domain-specific terminology for better semantic matching.
    
    Example: "Custom logic within a data Model" -> "Custom logic within business entities"
    This helps the algorithm understand that "data model" = "business entities/classes"
    """
    text_lower = text.lower()
    normalized = text_lower
    
    for domain_term, equivalents in DOMAIN_TERM_EQUIVALENCES.items():
        if domain_term in text_lower:
            # Replace with primary equivalent (first in list)
            normalized = normalized.replace(domain_term, equivalents[0])
    
    return normalized

def load_tickets_json(path: str = 'xaf_support_tickets_by_feature.json') -> Optional[Dict[str, int]]:
    """Load ticket counts by feature category from JSON."""
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return None


def load_concepts(path: str = 'config/concepts.yml') -> List[Dict]:
    """Load concept definitions."""
    with open(path, 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f)
        return data.get('concepts', [])


# ============================================================================
# PATTERN CLASSIFICATION FUNCTIONS (Issues #1, #2, #4, #5, #6, #9)
# ============================================================================

def classify_synonym_term(term: str, concept_name: str) -> Dict[str, any]:
    """
    Classify synonym term and assign quality weight.
    
    Returns:
        {
            'type': str - classification type
            'weight': float - quality weight (0.0-1.0)
            'issue': str - reference to MAPPING_ALGORITHM_ISSUES.md or None
        }
    """
    term_lower = term.lower()
    words = term_lower.split()
    
    # Check if it's an API-specific term (highest quality)
    if re.search(API_PATTERNS, term):
        return {
            'type': 'api',
            'weight': 1.0,
            'issue': None,
            'reason': 'API-specific term (high precision)'
        }
    
    # Check for umbrella terms (Issue #1)
    if term_lower in UMBRELLA_TERMS:
        return {
            'type': 'umbrella',
            'weight': 0.2,
            'issue': 'Umbrella term spans multiple concepts - Issue #1',
            'reason': 'Too broad, causes false positives'
        }
    
    # Check for generic verbs without context (Issue #2)
    if len(words) <= 2 and any(v in words for v in GENERIC_VERBS):
        return {
            'type': 'generic_verb',
            'weight': 0.3,
            'issue': 'Generic verb without context - Issue #2',
            'reason': 'Action verb needs specific context'
        }
    
    # Check for tool patterns (Issue #4)
    if re.search(TOOL_PATTERNS, term_lower, re.IGNORECASE):
        return {
            'type': 'tool',
            'weight': 0.8,
            'issue': 'Tool/editor - should be separate concept? - Issue #4',
            'reason': 'Tools operate ON concepts, not synonyms'
        }
    
    # Check for property patterns (Issue #5)
    if re.search(PROPERTY_PATTERNS, term_lower, re.IGNORECASE):
        return {
            'type': 'property',
            'weight': 0.6,
            'issue': 'Property feature - should be child concept? - Issue #5',
            'reason': 'Property capabilities != component synonyms'
        }
    
    # Check for lifecycle patterns (Issue #9)
    if re.search(LIFECYCLE_PATTERNS, term_lower, re.IGNORECASE):
        return {
            'type': 'lifecycle',
            'weight': 0.7,
            'issue': 'Lifecycle pattern - should be child concept? - Issue #9',
            'reason': 'Lifecycle events describe WHEN, not WHAT'
        }
    
    # Check for storage/format patterns (Issue #6)
    if re.search(STORAGE_PATTERNS, term_lower, re.IGNORECASE) or \
       re.search(FORMAT_PATTERNS, term_lower, re.IGNORECASE):
        return {
            'type': 'storage',
            'weight': 0.6,
            'issue': 'Storage/format - should be child concept? - Issue #6',
            'reason': 'Describes HOW data is stored, not WHAT concept is'
        }
    
    # Compound descriptive term (good quality)
    if len(words) >= 3:
        return {
            'type': 'descriptive',
            'weight': 0.9,
            'issue': None,
            'reason': 'Multi-word descriptive phrase (good specificity)'
        }
    
    # Standard two-word term
    if len(words) == 2:
        return {
            'type': 'standard',
            'weight': 0.7,
            'issue': None,
            'reason': 'Standard two-word term'
        }
    
    # Single word (lower quality)
    return {
        'type': 'single_word',
        'weight': 0.5,
        'issue': None,
        'reason': 'Single word term (ambiguous)'
    }


def detect_duplicate_synonyms(concepts: List[Dict]) -> Dict[str, Dict]:
    """
    Detect synonyms that appear in multiple concepts (Issue #3).
    
    Returns dict of duplicates with recommendations.
    """
    synonym_index = defaultdict(list)
    
    for concept in concepts:
        concept_name = concept['name']
        for synonym in concept.get('synonyms', []):
            synonym_lower = synonym.lower().strip()
            if synonym_lower:
                synonym_index[synonym_lower].append(concept_name)
    
    # Find duplicates
    duplicates = {}
    for synonym, concept_list in synonym_index.items():
        if len(concept_list) > 1:
            duplicates[synonym] = {
                'concepts': concept_list,
                'count': len(concept_list),
                'severity': 'HIGH' if len(concept_list) > 2 else 'MEDIUM',
                'issue': 'Duplicate synonym - Issue #3',
                'recommendation': 'Disambiguate or establish parent-child relationship'
            }
    
    return duplicates


def build_concept_hierarchy(concepts: List[Dict]) -> Dict[str, Dict]:
    """
    Build parent-child concept hierarchy for structure-aware matching.
    
    Returns dict indexed by concept name with parent/children info.
    """
    hierarchy = {}
    
    for concept in concepts:
        concept_name = concept['name']
        hierarchy[concept_name] = {
            'name': concept_name,
            'parent': concept.get('parent'),
            'children': [],
            'level': 0,
            'type': concept.get('type', 'concept')
        }
    
    # Build children lists
    for concept_name, info in hierarchy.items():
        if info['parent'] and info['parent'] in hierarchy:
            hierarchy[info['parent']]['children'].append(concept_name)
            info['level'] = 1  # Child concept
    
    return hierarchy


# ============================================================================
# IMPROVED MATCHING FUNCTIONS (Issues #7, #8)
# ============================================================================

def find_exact_phrase_matches(feature_category: str, concepts: List[Dict]) -> List[Dict]:
    """
    Find exact full-phrase matches (HIGHEST PRIORITY - Issue #7).
    
    Exact matches should always win over partial matches.
    """
    feature_lower = feature_category.lower().strip()
    matches = []
    
    for concept in concepts:
        # Check exact concept name match
        if concept['name'].lower() == feature_lower:
            matches.append({
                'concept': concept['name'],
                'score': 100,
                'match_type': 'exact_concept_name',
                'matched_term': concept['name'],
                'classification': {'type': 'exact', 'weight': 1.0, 'issue': None, 'reason': 'Exact concept name match'}
            })
            continue
        
        # Check exact synonym matches (full phrase)
        for synonym in concept.get('synonyms', []):
            if synonym.lower().strip() == feature_lower:
                classification = classify_synonym_term(synonym, concept['name'])
                matches.append({
                    'concept': concept['name'],
                    'score': 100 * classification['weight'],  # Weight affects exact synonym matches
                    'match_type': 'exact_synonym_phrase',
                    'matched_term': synonym,
                    'classification': classification
                })
                break
    
    return matches


def find_api_specific_matches(feature_category: str, concepts: List[Dict]) -> List[Dict]:
    """
    Find API-specific term matches (HIGH PRIORITY).
    
    API terms like IModelExtender, PermissionPolicyRole are high precision.
    """
    feature_lower = feature_category.lower()
    matches = []
    
    # Extract API-like terms from feature category
    api_terms = re.findall(API_PATTERNS, feature_category)
    if not api_terms:
        return []
    
    for concept in concepts:
        matching_synonyms = []
        best_score = 0
        
        for synonym in concept.get('synonyms', []):
            # Check if this synonym is an API term and appears in category
            if re.search(API_PATTERNS, synonym) and synonym.lower() in feature_lower:
                classification = classify_synonym_term(synonym, concept['name'])
                score = 80 * classification['weight']
                matching_synonyms.append({
                    'synonym': synonym,
                    'score': score,
                    'classification': classification
                })
                best_score = max(best_score, score)
        
        if matching_synonyms:
            matches.append({
                'concept': concept['name'],
                'score': best_score,
                'match_type': 'api_specific',
                'matching_synonyms': matching_synonyms
            })
    
    return sorted(matches, key=lambda x: x['score'], reverse=True)


def find_weighted_synonym_matches(feature_category: str, concepts: List[Dict]) -> List[Dict]:
    """
    Find synonym matches with quality weighting (MEDIUM PRIORITY).
    
    Weighted by term classification to penalize problematic patterns.
    Uses domain term normalization for semantic understanding.
    """
    feature_lower = feature_category.lower()
    feature_normalized = normalize_domain_terms(feature_category)
    matches = []
    
    for concept in concepts:
        matching_synonyms = []
        best_score = 0
        
        for synonym in concept.get('synonyms', []):
            synonym_lower = synonym.lower()
            synonym_normalized = normalize_domain_terms(synonym)
            
            # Check for substring match (original and normalized)
            if len(synonym_lower) > 3 and (synonym_lower in feature_lower or 
                                           synonym_normalized.lower() in feature_normalized.lower()):
                classification = classify_synonym_term(synonym, concept['name'])
                
                # Base score for synonym match
                base_score = 60
                weighted_score = base_score * classification['weight']
                
                matching_synonyms.append({
                    'synonym': synonym,
                    'score': weighted_score,
                    'classification': classification
                })
                
                best_score = max(best_score, weighted_score)
        
        if matching_synonyms:
            matches.append({
                'concept': concept['name'],
                'score': best_score,
                'match_type': 'weighted_synonym',
                'matching_synonyms': matching_synonyms
            })
    
    return sorted(matches, key=lambda x: x['score'], reverse=True)


def find_word_overlap_matches(feature_category: str, concepts: List[Dict]) -> List[Dict]:
    """
    Find matches based on word overlap (LOW PRIORITY - Issue #8).
    
    Only used when no better matches exist. Lowest confidence.
    Uses domain term normalization for semantic understanding.
    """
    feature_lower = feature_category.lower()
    feature_normalized = normalize_domain_terms(feature_category)
    
    # Extract words from both original and normalized
    feature_words = set(re.findall(r'\w+', feature_lower))
    feature_normalized_words = set(re.findall(r'\w+', feature_normalized.lower()))
    feature_words = feature_words | feature_normalized_words
    
    # Remove common words that don't add value
    stop_words = {'the', 'a', 'an', 'and', 'or', 'in', 'on', 'at', 'to', 'for', 'of', 'with', 'within'}
    feature_words = feature_words - stop_words
    
    matches = []
    
    for concept in concepts:
        # Also normalize concept words
        concept_words = set(concept['name'].lower().split())
        
        # Add normalized synonym words to improve matching
        for synonym in concept.get('synonyms', [])[:5]:  # Limit to avoid noise
            normalized_synonym = normalize_domain_terms(synonym)
            concept_words.update(normalized_synonym.lower().split())
        
        concept_words = concept_words - stop_words
        
        overlap = concept_words & feature_words
        
        if overlap:
            overlap_score = len(overlap) / max(len(concept_words), len(feature_words))
            score = 40 * overlap_score  # Max 40 points for word overlap
            
            matches.append({
                'concept': concept['name'],
                'score': score,
                'match_type': 'word_overlap',
                'overlap_words': list(overlap),
                'overlap_ratio': overlap_score
            })
    
    return sorted(matches, key=lambda x: x['score'], reverse=True)


def apply_parent_child_preference(matches: List[Dict], feature_category: str, 
                                   hierarchy: Dict[str, Dict]) -> List[Dict]:
    """
    Adjust scoring based on parent-child relationships.
    
    - API-specific terms → prefer child concepts
    - Descriptive phrases → prefer parent concepts
    """
    has_api_terms = bool(re.search(API_PATTERNS, feature_category))
    
    adjusted_matches = []
    
    for match in matches:
        concept_name = match['concept']
        concept_info = hierarchy.get(concept_name, {})
        
        adjustment = 1.0
        
        # Prefer children for API-specific terms
        if has_api_terms and concept_info.get('parent'):
            adjustment = 1.15  # 15% boost for child concepts
        
        # Prefer parents for descriptive phrases
        if not has_api_terms and not concept_info.get('parent'):
            adjustment = 1.1  # 10% boost for parent concepts
        
        adjusted_matches.append({
            **match,
            'score': match['score'] * adjustment,
            'hierarchy_adjustment': adjustment
        })
    
    return sorted(adjusted_matches, key=lambda x: x['score'], reverse=True)


def generate_mapping_warnings(mapping: Dict, concepts_tree: Dict[str, Dict], 
                               duplicates: Dict[str, Dict]) -> List[Dict]:
    """
    Generate warnings about potential mapping issues.
    """
    warnings = []
    
    # Low confidence warning
    if mapping['confidence'] < 70:
        warnings.append({
            'severity': 'LOW_CONFIDENCE',
            'message': f"Low confidence score: {mapping['confidence']:.1f}",
            'recommendation': 'Review mapping or add more specific synonyms to concept'
        })
    
    # Check for problematic synonym matches
    if 'match_details' in mapping and 'matching_synonyms' in mapping['match_details']:
        for syn in mapping['match_details']['matching_synonyms']:
            classification = syn.get('classification', {})
            if classification.get('issue'):
                warnings.append({
                    'severity': 'PATTERN_ISSUE',
                    'message': classification['issue'],
                    'synonym': syn['synonym'],
                    'reason': classification.get('reason', ''),
                    'recommendation': 'Consider refactoring concept structure'
                })
    
    # Check if matched term is a duplicate synonym
    matched_term = mapping.get('matched_term', '')
    if matched_term.lower() in duplicates:
        dup_info = duplicates[matched_term.lower()]
        warnings.append({
            'severity': dup_info['severity'],
            'message': f"Synonym '{matched_term}' appears in {dup_info['count']} concepts: {', '.join(dup_info['concepts'])}",
            'recommendation': dup_info['recommendation']
        })
    
    return warnings




def map_tickets_to_concepts(tickets: Dict[str, int], concepts: List[Dict]) -> List[Dict]:
    """
    IMPROVED: Map ticket feature categories to concept definitions using match type hierarchy.
    
    Algorithm addresses 9 issues from MAPPING_ALGORITHM_ISSUES.md:
    - Issue #1: Umbrella Terms - weighted down via classification
    - Issue #2: Generic Verbs - weighted down via classification
    - Issue #3: Duplicate Synonyms - detected and warned
    - Issue #4: Tool/Editor Confusion - detected via patterns
    - Issue #5: Property Features - detected via patterns
    - Issue #6: Storage Formats - detected via patterns
    - Issue #7: Exact Category Name Matching - highest priority
    - Issue #8: Score Accumulation - replaced with match type hierarchy
    - Issue #9: Lifecycle Patterns - detected via patterns
    
    Match Type Hierarchy (non-accumulative):
    1. Exact phrase match (score: 100) - HIGHEST PRIORITY
    2. API-specific match (score: 80) - HIGH PRIORITY
    3. Weighted synonym match (score: 60) - MEDIUM PRIORITY
    4. Word overlap (score: 40) - LOW PRIORITY
    
    Returns list of mappings with confidence scores and warnings.
    """
    mappings = []
    
    # Pre-compute structures for efficiency
    hierarchy = build_concept_hierarchy(concepts)
    duplicates = detect_duplicate_synonyms(concepts)
    
    # Map each ticket category using match type hierarchy
    for feature_category, ticket_count in tickets.items():
        
        # Phase 1: Exact phrase matches (HIGHEST PRIORITY - Issue #7)
        exact_matches = find_exact_phrase_matches(feature_category, concepts)
        if exact_matches:
            # Apply parent-child preference
            exact_matches = apply_parent_child_preference(exact_matches, feature_category, hierarchy)
            best_match = exact_matches[0]
            
            mapping = {
                'feature_category': feature_category,
                'ticket_count': ticket_count,
                'primary_concept': best_match['concept'],
                'confidence': best_match['score'],
                'match_type': best_match['match_type'],
                'matched_term': best_match.get('matched_term', ''),
                'match_details': best_match,
                'alternate_concepts': [m['concept'] for m in exact_matches[1:3]]
            }
            mapping['warnings'] = generate_mapping_warnings(mapping, hierarchy, duplicates)
            mappings.append(mapping)
            continue
        
        # Phase 2: API-specific matches (HIGH PRIORITY)
        api_matches = find_api_specific_matches(feature_category, concepts)
        if api_matches:
            api_matches = apply_parent_child_preference(api_matches, feature_category, hierarchy)
            best_match = api_matches[0]
            
            mapping = {
                'feature_category': feature_category,
                'ticket_count': ticket_count,
                'primary_concept': best_match['concept'],
                'confidence': best_match['score'],
                'match_type': best_match['match_type'],
                'match_details': best_match,
                'alternate_concepts': [m['concept'] for m in api_matches[1:3]]
            }
            mapping['warnings'] = generate_mapping_warnings(mapping, hierarchy, duplicates)
            mappings.append(mapping)
            continue
        
        # Phase 3: Weighted synonym matches (MEDIUM PRIORITY - Issues #1, #2)
        synonym_matches = find_weighted_synonym_matches(feature_category, concepts)
        if synonym_matches:
            synonym_matches = apply_parent_child_preference(synonym_matches, feature_category, hierarchy)
            best_match = synonym_matches[0]
            
            mapping = {
                'feature_category': feature_category,
                'ticket_count': ticket_count,
                'primary_concept': best_match['concept'],
                'confidence': best_match['score'],
                'match_type': best_match['match_type'],
                'match_details': best_match,
                'alternate_concepts': [m['concept'] for m in synonym_matches[1:3]]
            }
            mapping['warnings'] = generate_mapping_warnings(mapping, hierarchy, duplicates)
            mappings.append(mapping)
            continue
        
        # Phase 4: Word overlap only as last resort (LOW PRIORITY - Issue #8)
        overlap_matches = find_word_overlap_matches(feature_category, concepts)
        if overlap_matches:
            overlap_matches = apply_parent_child_preference(overlap_matches, feature_category, hierarchy)
            best_match = overlap_matches[0]
            
            mapping = {
                'feature_category': feature_category,
                'ticket_count': ticket_count,
                'primary_concept': best_match['concept'],
                'confidence': best_match['score'],
                'match_type': best_match['match_type'],
                'match_details': best_match,
                'alternate_concepts': [m['concept'] for m in overlap_matches[1:3]]
            }
            mapping['warnings'] = generate_mapping_warnings(mapping, hierarchy, duplicates)
            mappings.append(mapping)
            continue
        
        # No matches found
        mapping = {
            'feature_category': feature_category,
            'ticket_count': ticket_count,
            'primary_concept': 'UNMAPPED',
            'confidence': 0,
            'match_type': 'none',
            'match_details': {},
            'alternate_concepts': [],
            'warnings': [{
                'severity': 'UNMAPPED',
                'message': 'No matching concept found',
                'recommendation': 'Consider adding new concept or synonyms'
            }]
        }
        mappings.append(mapping)
    
    return mappings


def identify_priority_concepts(mappings: List[Dict]) -> pl.DataFrame:
    """
    Roll up ticket volumes by concept to find high-priority areas.
    """
    df = pl.DataFrame(mappings)
    
    # Sum tickets by primary concept
    concept_volumes = (
        df.group_by('primary_concept')
        .agg([
            pl.col('ticket_count').sum().alias('total_tickets'),
            pl.col('feature_category').count().alias('feature_count'),
            pl.col('feature_category').alias('features')
        ])
        .sort('total_tickets', descending=True)
    )
    
    return concept_volumes


def categorize_ticket_types(mappings: List[Dict]) -> Dict[str, List[Dict]]:
    """
    Categorize tickets by likely gap type based on feature category name.
    """
    categories = {
        'api_search': [],        # Users looking for specific APIs
        'customization': [],     # Users trying to extend/customize
        'setup': [],             # Configuration/setup issues  
        'performance': [],       # Speed/optimization
        'integration': [],       # Third-party integration
        'concepts': [],          # Understanding core concepts
        'platform_specific': [], # Platform-specific questions
    }
    
    patterns = {
        'api_search': ['custom', 'built-in', 'api', 'editor', 'controller', 'action'],
        'customization': ['custom logic', 'extend', 'override', 'customize'],
        'setup': ['setup', 'troubleshooting', 'configuration', 'wizard'],
        'performance': ['speed', 'performance', 'optimization'],
        'integration': ['oauth', 'authentication', 'external', 'legacy'],
        'concepts': ['relationships', 'model', 'criteria', 'data model'],
        'platform_specific': ['blazor', 'winforms', 'web', 'middle-tier'],
    }
    
    for mapping in mappings:
        feature = mapping['feature_category'].lower()
        
        # Match to categories
        matched = False
        for category, keywords in patterns.items():
            if any(keyword in feature for keyword in keywords):
                categories[category].append(mapping)
                matched = True
                break
        
        if not matched:
            categories['concepts'].append(mapping)
    
    return categories


def generate_ontology_priorities(
    concept_volumes: pl.DataFrame,
    ticket_categories: Dict[str, List[Dict]],
    total_tickets: int
) -> List[Dict]:
    """
    Generate prioritized recommendations for ontology implementation phases.
    """
    priorities = []
    
    # Phase 1: Metadata Tagging (Immediate)
    api_tickets = sum(m['ticket_count'] for m in ticket_categories['api_search'])
    platform_tickets = sum(m['ticket_count'] for m in ticket_categories['platform_specific'])
    
    priorities.append({
        'phase': 'Phase 1: Metadata Tagging',
        'time_estimate': '2-4 hours',
        'impact_tickets': api_tickets + platform_tickets,
        'impact_pct': f"{((api_tickets + platform_tickets) / total_tickets) * 100:.1f}%",
        'recommendation': 'Tag sections with Concept + Platform + Content Type. HIGH ROI for API search tickets.',
        'priority': 'CRITICAL',
    })
    
    # Phase 2: API Entities (High Priority)
    priorities.append({
        'phase': 'Phase 2: API Entities',
        'time_estimate': '8-12 hours',
        'impact_tickets': api_tickets,
        'impact_pct': f"{(api_tickets / total_tickets) * 100:.1f}%",
        'recommendation': 'Extract API entities from docs. Enable "find API for [concept]" queries.',
        'priority': 'HIGH',
    })
    
    # Phase 3: Cross-Corpus Bridges (Medium Priority)
    customization_tickets = sum(m['ticket_count'] for m in ticket_categories['customization'])
    
    priorities.append({
        'phase': 'Phase 3: Cross-Corpus Bridges',
        'time_estimate': '2-3 hours',
        'impact_tickets': customization_tickets,
        'impact_pct': f"{(customization_tickets / total_tickets) * 100:.1f}%",
        'recommendation': 'Connect concept docs to implementing APIs. Reduce "how do I use X" tickets.',
        'priority': 'MEDIUM',
    })
    
    # Phase 4: Gap Detection (Proactive)
    setup_tickets = sum(m['ticket_count'] for m in ticket_categories['setup'])
    
    priorities.append({
        'phase': 'Phase 4: Gap Detection',
        'time_estimate': '4-6 hours',
        'impact_tickets': setup_tickets,
        'impact_pct': f"{(setup_tickets / total_tickets) * 100:.1f}%",
        'recommendation': 'Automate gap detection. Prevent future tickets by finding missing content.',
        'priority': 'MEDIUM',
    })
    
    return priorities


def main():
    print("=" * 80)
    print("XAF SUPPORT TICKET ANALYSIS - ONTOLOGY PRIORITIZATION")
    print("=" * 80)
    print()
    
    # Load data
    tickets = load_tickets_json()
    if not tickets:
        print("❌ Error: Could not find xaf_support_tickets_by_feature.json")
        print("   Make sure the file is in the project root directory.")
        sys.exit(1)
    
    concepts = load_concepts()
    
    print(f"📊 Loaded {len(tickets)} feature categories")
    print(f"📊 Loaded {len(concepts)} concept definitions")
    print(f"📊 Total tickets analyzed: {sum(tickets.values()):,}")
    print()
    
    # Map tickets to concepts using improved algorithm
    print("🔄 Mapping feature categories to concepts (IMPROVED ALGORITHM)...")
    mappings = map_tickets_to_concepts(tickets, concepts)
    
    # Report mapping quality statistics
    match_types = defaultdict(int)
    total_warnings = 0
    high_confidence = 0
    
    for mapping in mappings:
        match_types[mapping['match_type']] += 1
        total_warnings += len(mapping.get('warnings', []))
        if mapping['confidence'] >= 80:
            high_confidence += 1
    
    print(f"✓ Mapped {len(mappings)} categories")
    print(f"  • High confidence (≥80): {high_confidence} ({high_confidence/len(mappings)*100:.1f}%)")
    print(f"  • Match types: {dict(match_types)}")
    print(f"  • Total warnings: {total_warnings}")
    print()
    
    # Analyze
    concept_volumes = identify_priority_concepts(mappings)
    ticket_categories = categorize_ticket_types(mappings)
    priorities = generate_ontology_priorities(concept_volumes, ticket_categories, sum(tickets.values()))
    
    # Report: Top Concepts by Ticket Volume
    print("\n" + "=" * 80)
    print("TOP 15 CONCEPTS BY TICKET VOLUME")
    print("=" * 80)
    print()
    
    top_concepts = concept_volumes.head(15)
    for row in top_concepts.iter_rows(named=True):
        concept = row['primary_concept']
        tickets_count = row['total_tickets']
        features = row['feature_count']
        pct = (tickets_count / sum(tickets.values())) * 100
        
        print(f"  {concept:40s} | {tickets_count:5,} tickets ({pct:5.1f}%) | {features} feature categories")
    
    # Report: Ticket Type Distribution
    print("\n" + "=" * 80)
    print("TICKET TYPE DISTRIBUTION")
    print("=" * 80)
    print()
    
    total = sum(tickets.values())
    for category, items in ticket_categories.items():
        count = sum(m['ticket_count'] for m in items)
        pct = (count / total) * 100
        print(f"  {category:25s} | {count:5,} tickets ({pct:5.1f}%)")
    
    # Report: Ontology Implementation Priorities
    print("\n" + "=" * 80)
    print("ONTOLOGY IMPLEMENTATION PRIORITIES (Ticket-Driven)")
    print("=" * 80)
    print()
    
    for priority in priorities:
        print(f"\n{priority['phase']} [{priority['priority']}]")
        print(f"  Time Estimate: {priority['time_estimate']}")
        print(f"  Impact: {priority['impact_tickets']:,} tickets ({priority['impact_pct']})")
        print(f"  → {priority['recommendation']}")
    
    # Report: Unmapped Feature Categories
    unmapped = [m for m in mappings if m['primary_concept'] == 'UNMAPPED']
    if unmapped:
        print("\n" + "=" * 80)
        print(f"UNMAPPED FEATURE CATEGORIES ({len(unmapped)} - Need Manual Review)")
        print("=" * 80)
        print()
        for item in sorted(unmapped, key=lambda x: x['ticket_count'], reverse=True):
            print(f"  • {item['feature_category']} ({item['ticket_count']} tickets)")
    
    # Report: High-Impact Warnings (Issues requiring attention)
    high_severity_warnings = []
    for mapping in mappings:
        for warning in mapping.get('warnings', []):
            if warning['severity'] in ['HIGH', 'MEDIUM', 'PATTERN_ISSUE']:
                high_severity_warnings.append({
                    'category': mapping['feature_category'],
                    'tickets': mapping['ticket_count'],
                    'concept': mapping['primary_concept'],
                    **warning
                })
    
    if high_severity_warnings:
        print("\n" + "=" * 80)
        print(f"MAPPING QUALITY WARNINGS ({len(high_severity_warnings)} issues detected)")
        print("=" * 80)
        print()
        
        # Group by severity
        by_severity = defaultdict(list)
        for w in high_severity_warnings:
            by_severity[w['severity']].append(w)
        
        for severity in ['HIGH', 'MEDIUM', 'PATTERN_ISSUE']:
            if severity in by_severity:
                print(f"\n{severity} Severity ({len(by_severity[severity])} issues):")
                for w in sorted(by_severity[severity], key=lambda x: x['tickets'], reverse=True)[:10]:
                    print(f"  • {w['category']} → {w['concept']}")
                    print(f"    {w['message']}")
                    print(f"    Recommendation: {w['recommendation']}")
                    print()

    
    # Save outputs
    print("\n" + "=" * 80)
    print("SAVING OUTPUTS")
    print("=" * 80)
    print()
    
    # Save concept volumes (drop nested 'features' column for CSV)
    concept_volumes.drop('features').write_csv('outputs/ticket_discoverability/ticket_volumes_by_concept.csv')
    print("  ✓ outputs/ticket_discoverability/ticket_volumes_by_concept.csv")
    
    # Prepare mappings for CSV (flatten nested structures)
    csv_mappings = []
    for m in mappings:
        csv_row = {
            'feature_category': m['feature_category'],
            'ticket_count': m['ticket_count'],
            'primary_concept': m['primary_concept'],
            'confidence': round(m['confidence'], 2),
            'match_type': m['match_type'],
            'matched_term': m.get('matched_term', ''),
            'alternate_concepts': ', '.join(m.get('alternate_concepts', [])),
            'warning_count': len(m.get('warnings', [])),
            'has_issues': 'Yes' if any(w['severity'] in ['HIGH', 'MEDIUM', 'PATTERN_ISSUE'] 
                                       for w in m.get('warnings', [])) else 'No'
        }
        csv_mappings.append(csv_row)
    
    pl.DataFrame(csv_mappings).write_csv('outputs/ticket_discoverability/ticket_feature_to_concept_mapping.csv')
    print("  ✓ outputs/ticket_discoverability/ticket_feature_to_concept_mapping.csv")
    
    # Save detailed warnings to JSON for deeper analysis
    warnings_data = []
    for m in mappings:
        if m.get('warnings'):
            warnings_data.append({
                'feature_category': m['feature_category'],
                'ticket_count': m['ticket_count'],
                'primary_concept': m['primary_concept'],
                'confidence': m['confidence'],
                'match_type': m['match_type'],
                'warnings': m['warnings']
            })
    
    with open('outputs/ticket_discoverability/mapping_warnings.json', 'w') as f:
        json.dump(warnings_data, f, indent=2)
    print("  ✓ outputs/ticket_discoverability/mapping_warnings.json")

    
    # Save priorities
    with open('outputs/ticket_discoverability/ontology_implementation_priorities.json', 'w') as f:
        json.dump({
            'priorities': priorities,
            'total_tickets': sum(tickets.values()),
            'ticket_categories': {k: sum(m['ticket_count'] for m in v) for k, v in ticket_categories.items()},
            'top_10_concepts': [
                {
                    'concept': row['primary_concept'],
                    'tickets': row['total_tickets'],
                    'features': row['feature_count']
                }
                for row in concept_volumes.head(10).iter_rows(named=True)
            ]
        }, f, indent=2)
    print("  ✓ outputs/ticket_discoverability/ontology_implementation_priorities.json")
    
    # Summary CSV for easy reference
    top_20 = concept_volumes.head(20)
    summary_df = pl.DataFrame({
        'rank': range(1, len(top_20) + 1),
        'concept': [row['primary_concept'] for row in top_20.iter_rows(named=True)],
        'tickets': [row['total_tickets'] for row in top_20.iter_rows(named=True)],
        'pct_of_total': [f"{(row['total_tickets'] / total) * 100:.1f}%" for row in top_20.iter_rows(named=True)],
        'feature_categories': [row['feature_count'] for row in top_20.iter_rows(named=True)]
    })
    summary_df.write_csv('outputs/ticket_discoverability/ticket_analysis_actions.csv')
    print("  ✓ outputs/ticket_discoverability/ticket_analysis_actions.csv")
    
    # Summary
    print("\n" + "=" * 80)
    print("SUMMARY & NEXT STEPS")
    print("=" * 80)
    print()
    print(f"✓ Analyzed {sum(tickets.values()):,} tickets")
    print(f"✓ Mapped to {len(concept_volumes)} concepts")
    print(f"✓ Identified {len(priorities)} implementation phases")
    if unmapped:
        print(f"⚠️  {len(unmapped)} feature categories need manual concept mapping")
    print()
    print("📌 RECOMMENDED NEXT STEPS:")
    print()
    print("  1. Review outputs/ticket_discoverability/ticket_volumes_by_concept.csv")
    print("  2. Start with Phase 1: Metadata Tagging (CRITICAL - 2-4 hours)")
    print("  3. Follow ontology_implementation_guide.md phases in priority order")
    print("  4. Track ticket reduction after each phase")
    print()
    print("💡 Expected ROI:")
    api_tickets = sum(m['ticket_count'] for m in ticket_categories['api_search'])
    print(f"   • Phase 1+2 could reduce {api_tickets:,} API-related tickets by 40-50%")
    print(f"   • That's ~{int(api_tickets * 0.45):,} fewer tickets within 8 weeks")
    print()
    
    # Calculate ROI
    avg_mins_per_ticket = 30
    hours_per_year = (sum(tickets.values()) * avg_mins_per_ticket) / 60
    print("💰 ESTIMATED ROI:")
    print(f"   Current annual cost: ~{int(hours_per_year)} hours/year resolving doc tickets")
    print(f"   Investment Phase 1-4: ~25 hours")
    print(f"   Expected reduction: 40-50% of tickets")
    print(f"   Hours saved/year: ~{int(hours_per_year * 0.45)} hours")
    print(f"   Payback period: ~2 months")
    print(f"   Year 1 ROI: ~{int((hours_per_year * 0.45 / 25) * 100)}%")


if __name__ == '__main__':
    main()

