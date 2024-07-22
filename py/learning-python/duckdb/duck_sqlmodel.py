from sqlalchemy import Column, Integer, Sequence, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm.session import Session

Base = declarative_base()


class FakeModel(Base):  # type: ignore
    __tablename__ = "fake"

    id = Column(Integer, Sequence("fakemodel_id_sequence"), primary_key=True)
    name = Column(String)


eng = create_engine("duckdb:///:memory:")
Base.metadata.create_all(eng)
session = Session(bind=eng)

session.add(FakeModel(name="Frank"))
session.commit()

frank = session.query(FakeModel).one()

assert frank.name == "Frank"


# from sqlmodel import SQLModel, Field, create_engine, Session

# class Item(SQLModel, table=True):
#     id: int = Field(default=None, primary_key=True)
#     name: str

# # DuckDBに接続
# engine = create_engine("duckdb:///:memory:")

# # テーブルを作成
# SQLModel.metadata.create_all(engine)

# # データを挿入
# with Session(engine) as session:
#     item = Item(name="Sample Item")
#     session.add(item)
#     session.commit()

# # データを取得
# with Session(engine) as session:
#     items = session.query(Item).all()
#     print(items)
