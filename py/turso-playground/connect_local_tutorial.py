"""
Tursoを使用したローカルデータベースのかんたんな操作
"""
import os
import libsql_experimental as libsql

# ローカル接続

conn = libsql.connect("./local_demo1.db")
cur = conn.cursor()

def exec_query():
    # クエリの実行
    conn.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER);")
    conn.execute("INSERT INTO users(id) VALUES (10);")
    conn.execute("INSERT INTO users(id) VALUES (20);")

    print(conn.execute("select * from users").fetchall())

def main():
    exec_query()


if __name__ == "__main__":
    main()
