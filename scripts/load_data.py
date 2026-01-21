import pandas as pd
import sqlite3

# 1. Read CSV file (with correct encoding)
df = pd.read_csv("data/sales.csv", encoding="latin1")

# 2. Connect to SQLite database (creates file if not exists)
conn = sqlite3.connect("database/sales.db")

# 3. Load DataFrame into SQL table
df.to_sql("sales", conn, if_exists="replace", index=False)

# 4. Confirm success
print("✅ Data loaded into SQLite database successfully!")

# 5. Close connection
conn.close()
