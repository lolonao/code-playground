from sqlmodel import SQLModel, Field, create_engine, Session
from sqlalchemy import Column, Integer
from typing import Optional

class Item(SQLModel, table=True):
    id: Optional[int] = Field(default=None, sa_column=Column(Integer, primary_key=True, autoincrement=True))
    name: str

# DuckDBに接続するためのエンジンを作成
engine = create_engine("duckdb:///example.db")

# テーブルを作成
SQLModel.metadata.create_all(engine)

# データを挿入
with Session(engine) as session:
    item = Item(name="Sample Item")
    session.add(item)
    session.commit()

# データを取得
with Session(engine) as session:
    items = session.query(Item).all()
    for item in items:
        print(f"ID: {item.id}, Name: {item.name}")

