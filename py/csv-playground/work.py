"""
Hitosara Tokyo BAR

id,name,hitosara_url,homepage_url,title,insta_url,summary
1,バー＆カフェ　カメリア,https://hitosara.com/0006085891/,http://www.tokyostationhotel.jp/restaurants/camellia/,東京ステーションホテル The Tokyo Station Hotel,https://www.instagram.com/tokyostationhotel/,カフェ&バー カメリアもこれまでと内装を変えダークピンクが印象的な設えへ、より ... バー＆カフェ カメリアでは、丸の内シティを眺めながらゆったりとアフタヌーン ...
"""
import sys
from time import sleep
# from datetime import datetime
from typing import Optional, List
from sqlmodel import Field, SQLModel, Session
from sqlmodel import create_engine, select
# import csv
import pandas as pd

csv_file = './data/hitosara-bar-tokyo.csv'
df = pd.read_csv(csv_file)

# モデルを定義
class HitosaraBarInfo(SQLModel, table=True):
    index: int | None = Field(default=None, primary_key=True)
    bar_id: int = Field(nullable=False)
    name: str = Field(nullable=False)
    hitosara_url: str = Field(nullable=False)
    homepage_url: Optional[str] = None
    title: str = Field(nullable=False)
    insta_url: str = Field(nullable=False, unique=True)
    summary: str = Field(nullable=False, unique=True)

# import CSV file to Pandas dataframe.
# DBへの接続を定義
sqlite_file_name = './data/insta-url.sqlite'
sqlite_url = f'sqlite:///{sqlite_file_name}'
engine = create_engine(sqlite_url, echo=True)

# テーブルを作成
SQLModel.metadata.create_all(engine)

def sqlmodel_to_df(objs: List[SQLModel]) -> pd.DataFrame:
    """Convert a SQLModel objects into a pandas DataFrame."""
    records = [i.dict() for i in objs]
    df = pd.DataFrame.from_records(records)
    return df


with Session(engine) as session:
    # print(df.head())
    df.to_sql(
        'hitosarabarinfo',
        engine,
        if_exists='replace',
        index=True,
        method='multi',
        chunksize=1000
    )
    session.commit()
