import csv
from sqlmodel import Field, SQLModel, Session
from sqlmodel import create_engine


class Paper(SQLModel, table=True):
    """論文の詳細情報"""
    id: int | None = Field(default=None, primary_key=True)
    category: str = Field(nullable=False)
    keyword: str = Field(nullable=False, unique=False)
    genre: str = Field(nullable=False)  # ジャンルは複数ある。 enum?
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


# DBへの接続を定義
SQLITE_FILE = './paper-info.sqlite'
sqlite_url = f'sqlite:///{SQLITE_FILE}'
engine = create_engine(sqlite_url, echo=False)


def create_db_and_tables() -> None:
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
    CSV_FILE = "./data/お金_日本語.csv"
    records = csv_to_dict(CSV_FILE)
    # print(len(records))
    # print(len(records), records[0]["検索キーワード"])

    create_db_and_tables()

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
