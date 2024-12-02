import MeCab
dic_path = '-d /usr/lib/x86_64-linux-gnu/mecab/dic/mecab-ipadic-neologd'
mecab = MeCab.Tagger(dic_path)

text = '私はラーメンが大好物です。'

mecab = MeCab.Tagger(dic_path)
# mecab = MeCab.Tagger()
par = mecab.parseToNode(text)
print(text)
print('----------')
print(type(par))

while par:
    print(par.surface)  # 形態素の出力
    print(par.feature)  # 品詞などの出力
    """ 次の単語へ """
    par = par.next
