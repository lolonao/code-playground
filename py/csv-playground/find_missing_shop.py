import sys
import csv

BASE_CSV: str = './data/hitosara.csv'
BEOFRE_CSV = 'hitosara-bar-tokyo.csv'
OUTPUT_CSV: str = 'hitosara-bar-tokyo-again.csv'


def csv_to_dict(csv_file_path: str):
    shops = []
    with open(csv_file_path, mode='r', encoding='utf-8') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        # {'id': '', 'name': '', 'area': '', 'keywords': '', 'hitosara_url': '', 'homepage_url': '', 'exception': '', 'memo': ''}
        for row in csv_reader:
            # print(row)
            shops.append(row)
    return shops


def is_registered_shop(shop_id: int) -> bool:
    """
    ショップIDが、当該csvファイルに存在するかどうかを返す関数
    TODO: shop[i] のIDが、got_shops配列に存在するかどうかチェック
    """
    print(f"ほげid: {shop_id}")
    got_shops = csv_to_dict('hitosara-bar-tokyo.csv')

    for shop in got_shops:
        print(f"2: {shop[0]}")
        if shop[shop_id] is None:  # shopが見つからない場合の処理を追加
            print("対象IDが見つからないから取得する必要がある。")
            return True
        else:
            print("対象がすでにある。")
    return False


def main():
    pass

if __name__ == "__main__":
    main()

