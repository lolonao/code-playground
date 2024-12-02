"""
Web ページのダウンロードと単語の切り出し
URL を指定して，Web ページをダウンロード．そして，確認表示を行う
"""
import urllib.request

r =  urllib.request.urlopen('https://www.kkaneko.jp')
html = r.read()
print(html.decode())

"""
HTML タグの除去
いまダウンロードした Web ページについて，BeautifulSoap を用いて，HTML タグを取り除く Python プログラム．テキストと JavaScript が残る．
"""

from bs4 import BeautifulSoup
soup = BeautifulSoup(html,'html5lib')
t = soup.get_text()
print(t)

# いまダウンロードした日本語の Web ページについて，MeCab を用いて，単語を切り出す Python プログラム

import sys
import MeCab
m = MeCab.Tagger("-Ochasen")
a = m.parse(t)
words = [i.split()[0] for i in a.splitlines()]
print(words)

