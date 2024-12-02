#ワードクラウドの作成
from wordcloud import WordCloud
 
fpath = "/Library/Fonts/ヒラギノ角ゴシック W3.ttc"
wordcloud = WordCloud(background_color="white",font_path=fpath,width=600,height=400,min_font_size=15)
wordcloud.generate(word)
 
wordcloud.to_file("./wordcloud.png")

###########################
# 余白の調整
###########################

wordcloud = WordCloud(background_color="white",font_path=fpath,width=600,height=400,min_font_size=15)


