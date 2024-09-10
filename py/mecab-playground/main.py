import MeCab

# A = MeCab.Tagger()
# text = 'pythonでMeCabを初めて使ってみます'
# result = A.parse(text)
# print(result)


wakati = MeCab.Tagger("-Owakati")
wakati.parse("pythonが大好きです").split()
# ['python', 'が', '大好き', 'です']

tagger = MeCab.Tagger()
print(tagger.parse("pythonが大好きです"))

# python  python  python  python  名詞-普通名詞-一般
# が      ガ      ガ      が      助詞-格助詞
# 大好き  ダイスキ        ダイスキ        大好き  形状詞-一般
# です    デス    デス    です    助動詞  助動詞-デス     終止形-一般
# EOS
