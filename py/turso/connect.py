import os
import libsql_experimental as libsql

# url = os.getenv("TURSO_DATABASE_URL")
# print(url)
# auth_token = os.getenv("TURSO_AUTH_TOKEN")
# print(auth_token)

TURSO_DATABASE_URL='libsql://my-db-lolonaoo.turso.io'
TURSO_AUTH_TOKEN='eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE3MjA2MDI2MzEsImlkIjoiZWM2YmM4M2YtMDE5NS00YTFlLWJhNjEtMGZiMTNjM2U3ZTAzIn0.B7Y8q4jMAL2YreLQhdqWjLn_Rxp2cszp87oZm7K5jYuh-FBDBMui9uqnJIfFAbKtBhS48HtkeH8vVPAIwQSPCA'

url = TURSO_DATABASE_URL
auth_token = TURSO_AUTH_TOKEN

# print(f'url: {url} token: {auth_token}')

# 接続

# Turso経由
conn = libsql.connect("hello.db", sync_url=url, auth_token=auth_token)
conn.sync()
cur = conn.cursor()

# ローカルのみ
# conn = libsql.connect("hello.db")
# cur = conn.cursor()

# 実行
conn.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER);")
conn.execute("INSERT INTO users(id) VALUES (10);")

print(conn.execute("select * from users").fetchall())
