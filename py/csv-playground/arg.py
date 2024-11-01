

#!/usr/bin/env python3
import argparse
import sys
from typing import Optional

def main() -> Optional[int]:
    """
    CLIアプリケーションのメインエントリーポイント
    Returns:
        int: 終了コード。成功時は0、エラー時は1
    """
    parser = argparse.ArgumentParser(description='論文検索CLIアプリケーション')
    subparsers = parser.add_subparsers(dest='command', help='利用可能なコマンド')

    # loginコマンドとその引数
    login_parser = subparsers.add_parser('login', help='ログイン処理を実行')
    login_parser.add_argument('--username', '-u', required=True, help='ユーザー名')
    login_parser.add_argument('--password', '-p', required=True, help='パスワード')

    # searchコマンドとその引数
    search_parser = subparsers.add_parser('search', help='論文検索を実行')
    search_parser.add_argument('--keyword', '-k', required=True, help='検索キーワード')
    search_parser.add_argument('--year', '-y', type=int, help='出版年で絞り込み')
    search_parser.add_argument('--limit', '-l', type=int, default=10, help='検索結果の最大件数（デフォルト: 10）')

    # detailコマンドとその引数
    detail_parser = subparsers.add_parser('detail', help='論文詳細情報を取得')
    detail_parser.add_argument('paper_id', help='論文ID')
    detail_parser.add_argument('--format', '-f', choices=['text', 'json'], default='text',
                              help='出力フォーマット（デフォルト: text）')

    args = parser.parse_args()

    try:
        if args.command == 'login':
            import login
            return login.main(username=args.username, password=args.password)
        
        elif args.command == 'search':
            import paper_search
            return paper_search.main(
                keyword=args.keyword,
                year=args.year,
                limit=args.limit
            )
        
        elif args.command == 'detail':
            import paper_detail
            return paper_detail.main(
                paper_id=args.paper_id,
                output_format=args.format
            )
        
        else:
            parser.print_help()
            return 1

    except Exception as e:
        print(f"エラーが発生しました: {str(e)}", file=sys.stderr)
        return 1

if __name__ == '__main__':
    sys.exit(main() or 0)

