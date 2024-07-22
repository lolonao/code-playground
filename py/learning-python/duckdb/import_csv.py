import duckdb
cursor = duckdb.connect()
print(cursor.execute('SELECT 42').fetchall())

import pandas as pd
import os
path = os.getcwd()
print(f"path: {path}")
df_airports = pd.read_csv(path + "/duckdb/trade-last-30-days.csv")

print(df_airports)

print(os.sep)
# /

print(os.sep is os.path.sep)
# True

