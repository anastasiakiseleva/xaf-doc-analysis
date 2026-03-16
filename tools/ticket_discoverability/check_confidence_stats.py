"""Calculate confidence score statistics from ticket mapping"""
import polars as pl

# Load the mapping
df = pl.read_csv('outputs/ticket_discoverability/ticket_feature_to_concept_mapping.csv')

# Calculate stats
total = len(df)
high_conf = df.filter(pl.col('confidence') >= 7)
perfect = df.filter(pl.col('confidence') == 10)
good = df.filter(pl.col('confidence') == 7)
weak = df.filter(pl.col('confidence') < 7)

print("=" * 80)
print("CONFIDENCE SCORE DISTRIBUTION")
print("=" * 80)
print(f"Total categories: {total}")
print(f"High confidence (7+): {len(high_conf)} ({len(high_conf)/total*100:.1f}%)")
print(f"  - Perfect match (10): {len(perfect)} ({len(perfect)/total*100:.1f}%)")
print(f"  - Good match (7): {len(good)} ({len(good)/total*100:.1f}%)")
print(f"Weak/No match (<7): {len(weak)} ({len(weak)/total*100:.1f}%)")
print()

# Calculate ticket coverage
total_tickets = df['ticket_count'].sum()
high_conf_tickets = high_conf['ticket_count'].sum()
perfect_tickets = perfect['ticket_count'].sum()

print("=" * 80)
print("TICKET COVERAGE BY CONFIDENCE")
print("=" * 80)
print(f"Total tickets: {total_tickets:,}")
print(f"High confidence (7+): {high_conf_tickets:,} ({high_conf_tickets/total_tickets*100:.1f}%)")
print(f"Perfect match (10): {perfect_tickets:,} ({perfect_tickets/total_tickets*100:.1f}%)")
