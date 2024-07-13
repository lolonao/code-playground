
参考

[SQLite互換サーバーレスDB Turso & FastAPI](https://zenn.dev/ikumasudo/articles/df8ab4fb01038c)

## 使い方

Turso CLIでデータベースを作成する。

```
turso db create DB名
```

データベースのURLを取得する。

```
turso db show --url DB名
```

データベースのトークンを取得する。

```
turso db tokens create DB名
```

SQLシェルに接続する。

```
turso db shell DB名
```


pip install fastapi sqlmodel

```
python -m venv .venv
source .vnev/bin/activate
pip install fastapi sqlmodel sqlalchemy sqlalchemy-libsql
```

## Links

- [クイックスタート - Turso](https://docs.turso.tech/quickstart)
- [Turso Quickstart (Python) - Turso](https://docs.turso.tech/sdk/python/quickstart)
