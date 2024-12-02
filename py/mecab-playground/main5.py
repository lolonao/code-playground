import MeCab

text = '私はラーメンが大好物です。'
mecab = MeCab.Tagger('-Oyomi')
me = mecab.parse(text)

print(me)
