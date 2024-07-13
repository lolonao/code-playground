"""
参照
​
埋め込みレプリカ
リモート データベースからローカル SQLite ファイルに同期し、
リモート プライマリ データベースへの書き込みを委任できる埋め込みレプリカを操作できます。

埋め込みレプリカは、ファイル システムにアクセスできる場合にのみ機能します。
"""

import os
import libsql_experimental as libsql

import dbconfig

db_name: str = "local.db"

url = dbconfig.DEMO1_TURSO_DATABASE_URL
auth_token = dbconfig.DEMO1_TURSO_AUTH_TOKEN
# print(f'url: {url} token: {auth_token}')

conn = libsql.connect(db_name, sync_url=url, auth_token=auth_token)


def embedded_replica():
    """
    リモート データベースからローカル SQLite ファイルに同期し、
    リモート プライマリ データベースへの書き込みを委任できる埋め込みレプリカを操作できます。
    """
    conn.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER);")
    conn.execute("INSERT INTO users(id) VALUES (1);")
    conn.commit()

    print(conn.execute("select * from users").fetchall())


def Periodic_synchronization():
    """
    定期的な同期
    オプションに秒単位の時間を渡すことで、間隔をあけて自動的に同期することができます。
    sync_interval。たとえば、1 分ごとに同期するには、次のコードを使用します。
    """
    conn = libsql.connect(db_name, sync_interval=60, sync_url=url, auth_token=auth_token)

def manual_synchronization():
    """
    手動同期
    このSync機能を使用すると、ローカル データベースをリモート データベースと手動で同期できます。
    """
    conn.execute("INSERT INTO users(id) VALUES (2);")
    conn.commit()
    conn.sync()

def encryption():
    """
    暗号化
    SQLite ファイルの暗号化を有効にするには、暗号化シークレットをencryption_keyオプションに渡します。

    暗号化されたデータベースは生データとして表示され、標準の SQLite データベースとして読み取ることはできません。
    すべての操作には libSQL クライアントを使用する必要があります。
    詳細は、このURLを参照。
    https://docs.turso.tech/libsql#encryption-at-rest
    """
    conn = libsql.connect("encrypted.db", sync_url=os.getenv("LIBSQL_URL"),
                      auth_token=os.getenv("LIBSQL_AUTH_TOKEN"),
                      encryption_key=os.getenv("ENCRYPTION_KEY"))
    