import MeCab


# 辞書を指定
mecab = MeCab.Tagger('-r /etc/mecabrc -d /usr/lib/x86_64-linux-gnu/mecab/dic/mecab-ipadic-neologd')
# mecab = MeCab.Tagger('-Owakati')

# print(mecab.parse('ポケモンGOが面白い'))

text: str = "『三国時代のナルシスト』 何晏が作り出した危険な快楽 「五石散」とは"
print(mecab.parse(text))
