"""
テストコード for SQLModel auto update
"""
from time import sleep
from datetime import datetime

from sqlmodel import Field, SQLModel, Session
from sqlmodel import create_engine, select


# モデルを定義
class User(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    created_at: datetime = Field(
        default_factory=datetime.now, nullable=False)
    updated_at: datetime = Field(
        default_factory=datetime.now, nullable=False,
        sa_column_kwargs={'onupdate': datetime.now})

# DBへの接続を定義
sqlite_file_name = "db1.sqlite"
sqlite_url = f"sqlite:///{sqlite_file_name}"
engine = create_engine(sqlite_url, echo=True)

# テーブルを作成
SQLModel.metadata.create_all(engine)

# Insert 1
with Session(engine) as session:
    user_1 = User(name='Taro')
    user_2 = User(name='Hanako')
    session.add(user_1)
    session.add(user_2)
    session.commit()

# 3秒Sleep
sleep(3)

with Session(engine) as session:
    user_3 = User(name='Jiro')
    session.add(user_3)
    session.commit()

# 3秒Sleep
sleep(3)

# Update
with Session(engine) as session:
    stmt = select(User)
    user = session.exec(stmt).first()
    if user is None:
        raise RuntimeError('user not found')
    user.name = 'Takashi'
    session.commit()

with Session(engine) as session:
    stmt = select(User)
    users = session.exec(stmt).all()
    print(users)

