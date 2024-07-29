import sys
import csv
import pandas as pd

"""
ヒトサラから取得したデータのヘッダ
id,name,area,keywords,hitosara_url,homepage_url,exception,memo
インスタグラム検索をした結果のデータのヘッダ
id,name,hitosara_url,homepage_url,title,insta_url,summary
"""

def csv_to_dict(csv_file_path: str):
    """CSVファイルの内容を辞書型で返す関数
    """
    shops = []
    with open(csv_file_path, mode='r', encoding='utf-8') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            # print(row)
            shops.append(row)
    return shops


def extract_missing_ids(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
    """
    CSVファイル1のIDが、CSVファイル2に存在しないデータを抽出します。

    Args:
        df1 (pd.DataFrame): CSVファイル1のデータ
        df2 (pd.DataFrame): CSVファイル2のデータ

    Returns:
        pd.DataFrame: CSVファイル1のIDがCSVファイル2に存在しないデータ
    """

    # IDの列を抽出
    ids1 = df1['id']
    ids2 = df2['id']

    # 型を統一（必要であれば）
    ids1 = ids1.astype(str)
    ids2 = ids2.astype(str)

    # missing_idsを抽出
    # missing_ids = ids1[~ids1.isin(ids2)].astype(int)  # int型に変換する場合

    # CSVファイル2に存在しないIDを抽出
    missing_ids = ids1[~ids1.isin(ids2)].astype(int)  # int型に変換

    # 抽出したIDに対応する行をCSVファイル1から抽出
    # result_df = df1[df1['id'].isin(missing_ids)]
    # result_df = df1[df1['id'].isin(missing_ids)].copy()
    # result_df = df1.loc[df1['id'].isin(missing_ids), :]
    result_df = df1.query("id in @missing_ids")

    return result_df


def main():
    BASE_CSV: str = './hitosara.csv'
    BEOFRE_CSV = './hitosara-bar-tokyo.csv'
    OUTPUT_CSV: str = 'hitosara-bar-tokyo-again.csv'

    # CSVファイルを読み込む
    df1 = pd.read_csv(BASE_CSV)
    df2 = pd.read_csv(BEOFRE_CSV)

    # 関数を呼び出して結果を取得
    result_df = extract_missing_ids(df1, df2)
    # 結果を出力 (CSVファイルとして保存)
    result_df.to_csv('result2.csv', index=False)
    # 結果を表示
    print(result_df)


if __name__ == "__main__":
    main()
