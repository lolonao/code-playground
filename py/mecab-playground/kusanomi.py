"""
TODO:
- [neologdn · PyPI](https://pypi.org/project/neologdn/)
- [Diatonic code - Blog](https://diatonic.codes/blog/neologdn/)
「NEologd辞書」をインストールする
!pip install neologdn
# テキストの正規化を行う「normalize」ライブラリを使って、下記のように動作確認をしましょう。
import neologdn
print(neologdn.normalize("ﾃﾞｨｰﾌﾟﾗｰﾆﾝｸﾞ"))


-Ochasenはmecabのオプションで出力モードになります。

mecabrc：デフォルト
-Ochasen：ChaSen互換
-Owakati：分かち書きのみ
-Oyomi：読みのみ（振り仮名）
-Odump：単語の全情報
"""

from io import TextIOWrapper
from sys import exception
# import MeCab
from MeCab import Tagger

"""
MeCab.Tagger("-d /システム辞書のpath")
MeCab.Tagger("-u /ユーザー辞書のpath")
-dと-uどちらの引数も指定しない場合は、デフォルトのシステム辞書である「IPA辞書」が使用されます。
"""
# 辞書を指定
# シェル上の辞書は`mecab -D`で明示的に確認できます。
config_path: str = '/etc/mecabrc'
dic_path: str = '/usr/lib/x86_64-linux-gnu/mecab/dic/mecab-ipadic-neologd'
# mecabTagger = MeCab.Tagger(f'-r {config_path} -d {dic_path} -Ochasen')  # 茶筌形式で出力
# mecabTagger = MeCab.Tagger('-Owakati')
# print(mecabTagger.parse('ポケモンGOが面白い'))

article_path: str = '1-洗い髪のお妻.txt'
# article_path: str = '2-自刃した武田勝頼に最期まで尽くした土屋昌恒 .txt'
textio: TextIOWrapper = open(article_path, 'r')
text: str = textio.read()


# print(mecabTagger.parse(text))

# node = mecab.parseToNode(text)

# while node:
#     word = node.surface
#     hinshi = node.feature.split(',')[0]
#     if hinshi == '名詞':
#         print(f"{word}: {node.feature}")
#         # print(node.feature.split(',')[6], node.feature.split(',')[7], node.feature.split(',')[8])
#     node = node.next

# mecab = MeCab.Tagger("-Ochasen")
# print(mecab.parse("すもももももももものうち"))
# import sys
# sys.exit(1)

# mecabTagger = MeCab.Tagger("-Owakati")  # 分かち書き
tagger = Tagger("-Ochasen")  # 茶筌形式で出力
# node = mecabTagger.parseToNode(text)
#  parseToNodeは、特定の品詞の単語だけを取り出したり、品詞ごとの使用回数をカウントしたりする場合に役立ちます。
node = tagger.parseToNode(text)

"""
surface：表層形
feature：品詞・品詞細分類1・品詞細分類2・品詞細分類3・活用形・活用型・原形・読み方・発音
"""

while node:
    try:
        # word = node.surface
        hinshi = node.feature.split(",")[0]
        hinshi2 = node.feature.split(",")[2]

        # if hinshi in ["名詞","人名"]:
        # if hinshi == '名詞' and hinshi2 == '人名':
        if hinshi == '名詞':
            if len(node.feature) > 6:
                # print(node.feature.split(',')[6], node.feature.split(',')[7], node.feature.split(',')[8])
                print(node.feature)
            # print(word+": "+hinshi)
    except Exception as e:
        # print(f"Error: {e}") # Almost Error: list index out of range
        pass
    finally:
        node = node.next

# TODO: CHECK
# pip install unidic-lite

"""
## Links
- [Google Colab で自然言語処理（＠大前研究室） – 機械学習の理論と応用を扱う研究室](http://int-info.com/index.php/google_collab_mecab/)
- [YouTube動画へのコメントをワードクラウドを使って表示する](https://zenn.dev/yebi_crab/articles/7e54c74fae120a)
- [Python で自然言語処理-MeCab](https://rinsaka.com/python/nltk/02-mecab.html)
"""


"""
表層形\t品詞,品詞細分類1,品詞細分類2,品詞細分類3,活用型,活用形,原形,読み,発音
FORMAT
https://taku910.github.io/mecab/

表層形：活用や表記揺れを考慮した、文章中で使用される単語形式
品詞：単語を文法上の形態や役割などから、「動詞・名詞・形容詞・形容動詞・副詞・連体詞・接続詞・感動詞・助動詞・助詞」へ分類したもの
品詞細分類1～3：辞書の品詞体系に基づいて品詞の属性をさらに分類したもの（名詞の場合には、固有名詞・人名・一般・組織・地域など）
活用型：単語の活用の仕方を分類したもの（動詞の場合は「五段活用・上一段活用・下一段活用・カ行変格活用・サ行変格活用」）
活用形：活用している動詞・形容詞・形容動詞・助動詞を「未然形・連用形・終止形・連体形・仮定形・命令形」へ分類したもの
原形：活用前の形式
読み方：単語のフリガナ（学習→ガクシュウ）
発音：日本語で発音する方法（学習→ガクシュー）

EX)
美人: 名詞,一般,*,*,*,*,美人,ビジン,ビジン
威厳: 名詞,一般,*,*,*,*,威厳,イゲン,イゲン
心持: 名詞,一般,*,*,*,*,心持,ココロモチ,ココロモチ
妻: 名詞,一般,*,*,*,*,妻,ツマ,ツマ
姉さん: 名詞,一般,*,*,*,*,姉さん,ネエサン,ネーサン
述懐: 名詞,サ変接続,*,*,*,*,述懐,ジュッカイ,ジュッカイ
凌雲: 名詞,固有名詞,人名,名,*,*,凌雲,リョウウン,リョーウン
閣: 名詞,固有名詞,組織,*,*,*,*
一: 名詞,数,*,*,*,*,一,イチ,イチ
回: 名詞,接尾,助数詞,*,*,*,回,カイ,カイ
東京: 名詞,固有名詞,地域,一般,*,*,東京,トウキョウ,トーキョー
百: 名詞,数,*,*,*,*,百,ヒャク,ヒャク
美人: 名詞,一般,*,*,*,*,美人,ビジン,ビジン
明治24年: 名詞,固有名詞,一般,*,*,*,明治24年,メイジニジュウヨネン,メイジニジュウヨネン
"""


"""
(ins) ❯ cat /etc/mecabrc
;
; Configuration file of MeCab
;
; $Id: mecabrc.in,v 1.3 2006/05/29 15:36:08 taku-ku Exp $;
;
; dicdir = /var/lib/mecab/dic/debian
dicdir = /usr/lib/x86_64-linux-gnu/mecab/dic/mecab-ipadic-neologd

; userdic = /home/foo/bar/user.dic

; output-format-type = wakati
; input-buffer-size = 8192

; node-format = %m\n
; bos-format = %S\n
; eos-format = EOS\n
"""


"""
[MeCabの「-Ochasen」使用時にエラーが出る場合 #error - Qiita](https://qiita.com/MOSO1409/items/3ec4672e52227a457349)
>>pip install ipadic

import ipadic

CHASEN_ARGS = r' -F "%m\t%f[7]\t%f[6]\t%F-[0,1,2,3]\t%f[4]\t%f[5]\n"'
CHASEN_ARGS += r' -U "%m\t%m\t%m\t%F-[0,1,2,3]\t\t\n"'

tagger = MeCab.Tagger(ipadic.MECAB_ARGS + CHASEN_ARGS)

print(tagger.parse("私がリンゴを食べました"))
"""
