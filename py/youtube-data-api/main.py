"""
[YouTube Data API  |  Google for Developers](https://developers.google.com/youtube/v3?hl=ja)
"""
import sys
import urllib.parse
import requests
from typing import List, Dict

API_KEY = 'AIzaSyDagN_qbT3QP6izJJo4Ttfyt0mfqUTVauo'  # YouTube Data API キーを設定してください
BASE_URL = 'https://www.googleapis.com/youtube/v3'

def search_videos(query: str, max_results: int = 5) -> List[Dict]:
    """
    YouTube で動画を検索する
    """
    params = {
        'part': 'snippet',
        'maxResults': max_results,
        'key': API_KEY,
        'q': query,
        'type': 'video'
    }
    
    try:
        response = requests.get(f'{BASE_URL}/search', params=params)
        response.raise_for_status()
        
        videos = []
        for item in response.json()['items']:
            video = {
                'id': item['id']['videoId'],
                'title': item['snippet']['title'],
                'channel': item['snippet']['channelTitle'],
                'description': item['snippet']['description'],
                'url': f'https://www.youtube.com/watch?v={item["id"]["videoId"]}'
            }
            videos.append(video)
        return videos
    
    except requests.exceptions.RequestException as e:
        print(f'エラーが発生しました: {e}')
        return []

def display_video(video: Dict) -> None:
    """
    動画情報を表示する
    """
    print('\n' + '='*50)
    print(f'タイトル: {video["title"]}')
    print(f'チャンネル: {video["channel"]}')
    print(f'URL: {video["url"]}')
    print(f'説明: {video["description"][:200]}...' if len(video["description"]) > 200 else video["description"])
    print('='*50)

def main():
    if len(sys.argv) < 2:
        print('使用方法: python youtube_cli.py <検索キーワード>')
        sys.exit(1)
    
    # コマンドライン引数から検索キーワードを取得
    search_query = ' '.join(sys.argv[1:])
    print(f'"{search_query}" の検索結果:')
    
    # 動画を検索
    videos = search_videos(search_query)
    
    if not videos:
        print('動画が見つかりませんでした。')
        return
    
    # 検索結果を表示
    for i, video in enumerate(videos, 1):
        print(f'\n[{i}]')
        display_video(video)

if __name__ == '__main__':
    main()
