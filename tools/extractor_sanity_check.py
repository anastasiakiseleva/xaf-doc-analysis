# peek_concepts_report.py
import pandas as pd
df = pd.read_parquet("outputs/doc_concepts.parquet", engine="pyarrow")

print("Rows:", len(df))
print("\nTop concepts:")
print(df.loc[df.kept, "concepts"].explode().value_counts().head(20))

print("\nTop APIs:")
print(df.loc[df.kept, "apis"].explode().value_counts().head(20))

print("\nTop platforms:")
print(df.loc[df.kept, "platforms"].explode().value_counts().head(10))

print("\nExamples of skipped (reasons):")
print(df.loc[~df.kept, "skip_reason"].value_counts().head(10))