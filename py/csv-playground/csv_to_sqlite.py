"""
論文情報が格納されているCSVファイルから、詳細情報をSQLite3のデータベースファイルにインポートする。
コンソールに表示されるのは、DBにインポートできない、壊れたレコードの情報のみ。
壊れたレコードは、ほとんどの場合、ちょっと修正するだけで良い。
"""
import csv
from sqlmodel import Field, SQLModel, Session, create_engine
import argparse


class Paper(SQLModel, table=True):
    """論文の詳細情報"""
    id: int | None = Field(default=None, primary_key=True)
    category: str = Field(nullable=False)
    keyword: str = Field(nullable=False, unique=False)
    genre: str = Field(nullable=False)
    title_e: str = Field(nullable=False)
    title_j: str = Field(nullable=False)
    consensus_url: str = Field(nullable=False)
    pdf_url: str = Field(nullable=False)
    published: str = Field(nullable=False)
    credit: str = Field(nullable=False)  # 大学名_機関名
    author: str = Field(nullable=False)
    key_takeaway: str = Field(nullable=False, unique=False)  # 重要なポイント
    abstract: str = Field(nullable=False, unique=False)
    citations: int = Field(nullable=False)  # 引用数
    check: int | None = 0


def create_db_and_tables(engine) -> None:
    # テーブルを作成
    SQLModel.metadata.create_all(engine)


def create_sample_paper() -> Paper:
    """サンプルのPaperを作成する"""
    return Paper(
        category = "ジャンル",
        keyword = "検索キーワード",
        genre = "",
        title_e = "論文タイトル",
        title_j = "論文タイトル（日本語）",
        consensus_url = "ConsensusURL",
        pdf_url = "引用論文URL",
        published = "発表時期",
        credit = "大学名・機関名",
        author = "著者名",
        key_takeaway = "要点",
        abstract = "要約",
        citations = 40,  ## "論文引用数
        check = 0
    )


def dict_to_paper_class(record: dict[str, str]) -> Paper:
    """
    辞書型配列の論文情報を、Papereクラスのオブジェクトに変換して返す

    CSVファイルのヘッダ

    ID,チェック,作業者,作業日,検索キーワード,論文タイトル,論文タイトル（日本語）,要点,要約,ジャンル,ConsensusURL,引用論文URL,発表時期,大学名・機関名,著者名,論文引用数,PDF,備考
    """
    # print(f"***** {record}")
    paper: Paper = Paper(category = record["ジャンル"],
        keyword = record["検索キーワード"],
        genre = record[""],
        title_e = record["論文タイトル"],
        title_j = record["論文タイトル（日本語）"],
        consensus_url = record["ConsensusURL"],
        pdf_url = record["引用論文URL"],
        published = record["発表時期"],
        credit = record["大学名・機関名"],
        author = record["著者名"],
        key_takeaway = record["要点"],
        abstract = record["要約"],
        citations = int(record["論文引用数"]),
        check = 0
    )

    return paper


def csv_to_dict(csv_file_path: str) -> list[dict[str, str]]:
    """
    CSVファイルの内容を辞書型の配列で返す関数

    Args:
    csv_file_path (str): CSVファイルのパス

    Returns:
    list[dict[str, str]]: CSVファイルの内容
    """
    records: list = []
    with open(csv_file_path, mode='r', encoding='utf-8') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            # print(f"タイプ: {type(row)}")
            # print(row)
            records.append(row)
    return records


def main():
    parser = argparse.ArgumentParser(description='指定された論文情報CSVファイルのデータをSQLiteデータベースにインポートするユーティリティ')
    # コマンドライン引数の処理
    parser.add_argument("csv_file", help="インポートするCSVファイル")
    # parser.add_argument("db_file", help="SQLiteデータベースファイル")
    args = parser.parse_args()

    # TODO: コマンドラインで出力先のデータベースファイルを指定する
    # DBへの接続を定義
    SQLITE_FILE = './paper-info.sqlite'
    sqlite_url = f'sqlite:///{SQLITE_FILE}'
    engine = create_engine(sqlite_url, echo=False)
    create_db_and_tables(engine)

    records = csv_to_dict(args.csv_file)
    for r in records:
        try:
            paper = dict_to_paper_class(r)
            with Session(engine) as session:
                session.add(paper)
                session.commit()
        except ValueError as v:
            print(f"正しくないレコード: {v} {r}\n\n")
            continue


if __name__ == "__main__":
    main()
