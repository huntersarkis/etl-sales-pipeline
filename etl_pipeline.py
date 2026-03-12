import pandas as pd
import sqlite3

# Extract
print("\nExtracting data...")
df = pd.read_csv("sales.csv")

# Transform
print("\nTransforming data...")
df["revenue"] = df["price"] * df["quantity"]

# Load
print("\nLoading data...")
conn = sqlite3.connect("sales.db")

df.to_sql("sales_clean", conn, if_exists="replace", index=False)

conn.close()

print("\nPipeline completed!")