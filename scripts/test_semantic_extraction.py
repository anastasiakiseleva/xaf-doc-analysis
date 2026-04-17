#!/usr/bin/env python
"""
Test the semantic concept extraction on the workflow-deployment false positive.
Exercises extract_concepts_semantic from 03_extract_concepts.py directly.
"""

import sys
import importlib.util
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from sentence_transformers import SentenceTransformer
from utils.taxonomy_loader import load_concepts

# 03_extract_concepts.py has a numeric prefix so we load it via importlib
_script_path = Path(__file__).parent / "03_extract_concepts.py"
_spec = importlib.util.spec_from_file_location("extract_concepts_module", _script_path)
_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mod)
extract_concepts_semantic = _mod.extract_concepts_semantic
compile_concept_index = _mod.compile_concept_index

# Sample text from workflow-design-basics that incorrectly gets tagged with "Deployment"
WORKFLOW_TEXT = """
Workflow Design Basics

To simplify workflow creation, the Workflow module ships with a built-in debugging 
functionality. You can debug workflows either while designing them or after deployment. 
To debug workflows while designing them, the Workflow module provides a set of specific 
Actions. These Actions are enabled after the current workflow definition has been loaded. 
To load a workflow definition, switch from the Properties page of a workflow definition 
to the workflow designer. This will enable debugging Actions.

To debug workflows after deploying them, use the Show Workflow Instances Action.

The Workflow module uses a State Machine to model business processes. You can define 
states, transitions, and actions in the workflow designer. When a workflow instance is 
created, it tracks the current state and available transitions.
"""

HEADING = "Workflow > Design Basics > Debugging"

# Sample deployment text (should match Deployment concept)
DEPLOYMENT_TEXT = """
Deploy ASP.NET Core Blazor Application to IIS

This guide explains how to deploy your XAF Blazor application to IIS on Windows Server.

Prerequisites:
- Windows Server with IIS installed
- .NET 8.0 Runtime or later
- SQL Server for the application database

Steps:
1. Configure IIS Application Pool
2. Install SSL certificate for HTTPS
3. Set up connection strings in appsettings.json
4. Deploy the application files
5. Configure database permissions

The deployment process requires proper security configuration including SSL certificates
and database authentication settings.
"""

DEPLOYMENT_HEADING = "Deployment > ASP.NET Core Blazor > Deploy to IIS"


def build_concept_index():
    """Build concept index from taxonomy using the production compile_concept_index."""
    concepts_cfg = load_concepts()
    concept_index = compile_concept_index(concepts_cfg)
    concepts_config = concepts_cfg.get('concepts', [])
    return concept_index, concepts_config


def test_semantic_extraction():
    """Test semantic extraction on workflow vs deployment text"""
    
    print("="*80)
    print("TESTING ENHANCED CONCEPT EXTRACTION")
    print("="*80)
    print()
    
    # Load model
    print("Loading embedding model...")
    model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
    
    # Load concepts
    print("Loading concept definitions...")
    concept_index, concepts_config = build_concept_index()
    
    print(f"  ✓ Loaded {len(concepts_config)} concepts")
    print()
    
    # Test 1: Workflow text (should NOT get Deployment tag)
    print("-"*80)
    print("TEST 1: Workflow Text (mentions 'deployment' casually)")
    print("-"*80)
    print(f"Heading: {HEADING}")
    print(f"Text snippet: {WORKFLOW_TEXT[:200]}...")
    print()
    
    concepts_wf, confidences_wf = extract_concepts_semantic(
        text=WORKFLOW_TEXT,
        heading=HEADING,
        concept_index=concept_index,
        concepts_config=concepts_config,
        model=model
    )
    
    print(f"Extracted {len(concepts_wf)} concepts:")
    for concept in concepts_wf[:15]:  # Top 15
        conf = confidences_wf.get(concept, 0.0)
        print(f"  • {concept:40s} (confidence: {conf:.3f})")
    
    if 'Deployment' in concepts_wf:
        print()
        print(f"  ⚠️  'Deployment' WAS TAGGED (confidence: {confidences_wf['Deployment']:.3f})")
        print("  This is the FALSE POSITIVE we're trying to fix")
    else:
        print()
        print("  ✅ 'Deployment' correctly suppressed!")
    
    print()
    
    # Test 2: Deployment text (SHOULD get Deployment tag)
    print("-"*80)
    print("TEST 2: Deployment Text (actually about deployment)")
    print("-"*80)
    print(f"Heading: {DEPLOYMENT_HEADING}")
    print(f"Text snippet: {DEPLOYMENT_TEXT[:200]}...")
    print()
    
    concepts_dep, confidences_dep = extract_concepts_semantic(
        text=DEPLOYMENT_TEXT,
        heading=DEPLOYMENT_HEADING,
        concept_index=concept_index,
        concepts_config=concepts_config,
        model=model
    )
    
    print(f"Extracted {len(concepts_dep)} concepts:")
    for concept in concepts_dep[:15]:  # Top 15
        conf = confidences_dep.get(concept, 0.0)
        print(f"  • {concept:40s} (confidence: {conf:.3f})")
    
    if 'Deployment' in concepts_dep:
        print()
        print(f"  ✅ 'Deployment' correctly tagged! (confidence: {confidences_dep['Deployment']:.3f})")
    else:
        print()
        print("  ⚠️  'Deployment' was NOT tagged - this is a FALSE NEGATIVE")
    
    print()
    print("="*80)
    print("SUMMARY")
    print("="*80)
    
    wf_has_deployment = 'Deployment' in concepts_wf
    dep_has_deployment = 'Deployment' in concepts_dep
    
    if not wf_has_deployment and dep_has_deployment:
        print("✅ PERFECT: Semantic validation working correctly!")
        print("   - Workflow text: Deployment suppressed")
        print("   - Deployment text: Deployment tagged")
    elif wf_has_deployment and dep_has_deployment:
        print("⚠️  PARTIAL: Still getting false positive on workflow")
        print("   May need to tune MIN_SEMANTIC_SIMILARITY threshold")
    elif not wf_has_deployment and not dep_has_deployment:
        print("⚠️  OVERCORRECTION: Suppressing too aggressively")
        print("   May need to lower MIN_CONCEPT_CONFIDENCE threshold")
    else:
        print("❌ BROKEN: Something is wrong with the logic")


if __name__ == "__main__":
    test_semantic_extraction()
