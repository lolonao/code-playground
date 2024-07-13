"""
Tursoを使用したリモートデータベースのかんたんな操作
"""
import os
import libsql_experimental as libsql

import dbconfig

# url = os.getenv("TURSO_DATABASE_URL")
# print(url)
# auth_token = os.getenv("TURSO_AUTH_TOKEN")
# print(auth_token)


url = dbconfig.DEMO1_TURSO_DATABASE_URL
auth_token = dbconfig.DEMO1_TURSO_AUTH_TOKEN

# print(f'url: {url} token: {auth_token}')

# 接続

# Turso経由
conn = libsql.connect("./local_demo1.db", sync_url=url, auth_token=auth_token)
conn.sync()

# クエリの実行
conn.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER);")
conn.execute("INSERT INTO users(id) VALUES (3);")
conn.execute("INSERT INTO users(id) VALUES (4);")

# 同期（埋め込みレプリカのみ）
# 埋め込みレプリカを使用する場合は、sync()コネクタを呼び出してローカル データベースをプライマリ データベースと同期する必要があります。

conn.commit()
conn.sync()

print(conn.execute("select * from users").fetchall())