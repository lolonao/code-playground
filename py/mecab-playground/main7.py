import MeCab

me = MeCab.Tagger ("-Ochasen")
text = open('自刃した武田勝頼に最期まで尽くした土屋昌恒 .txt', 'r')
txt_data = text.read()

print(me.parse (txt_data))

