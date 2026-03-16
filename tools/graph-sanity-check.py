import pandas as pd

edges = pd.read_parquet("outputs/explicit_graph.parquet", engine="pyarrow")

print("Edges:", len(edges))
print("Self-loops:", ((edges["source_doc"] == edges["target_doc"]).sum()))
print("Unique pairs:", len(edges[["source_doc","target_doc"]].drop_duplicates()))
print("Count distribution (top 5):")
print(edges["count"].value_counts().head())

# Top hubs and orphans
out_deg = edges.groupby("source_doc")["count"].sum().sort_values(ascending=False)
in_deg  = edges.groupby("target_doc")["count"].sum().sort_values(ascending=False)
print("\nTop out-degree:\n", out_deg.head(10))
print("\nTop in-degree:\n", in_deg.head(10))

docs = pd.read_parquet("outputs/topics_inventory.parquet", engine="pyarrow")
all_docs = set(docs["doc_id"].astype(str))
with_out = set(out_deg.index)
with_in  = set(in_deg.index)
orphans  = sorted(all_docs - (with_out | with_in))
print("\nOrphan docs:", len(orphans))