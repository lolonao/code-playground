# mecab-playground

## Pythonパッケージのインストール

PythonからMeCabを使用するために、mecab-python3パッケージをインストールします。

```
rye add mecab-python3
rye sync
```

## 辞書のインストール場所を表示する

```bash
echo `mecab-config --dicdir`"/mecab-ipadic-neologd"

/usr/lib/x86_64-linux-gnu/mecab/dic/mecab-ipadic-neologd
```


## 環境変数を設定する

PythonからMeCabを使用するためには、環境変数の設定が必要です。zshを使用している場合は、~/.bashrcにパスを設定します。

```
export MECABRC=/usr/local/etc/mecabrc
```

実行してみる

以下のように表示されれば、正しく使えている。

```python
import MeCab
mecab = MeCab.Tagger('-Owakati')
print(mecab.parse('ポケモンGOが面白い'))

# 出力結果： ポケモンGO が 面白い``python

```

## Links

### 公式

- [mecab-python3 · PyPI](https://pypi.org/project/mecab-python3/)
[mecab-ipadic-neologd/README.ja.md at master · neologd/mecab-ipadic-neologd](https://github.com/neologd/mecab-ipadic-neologd/blob/master/README.ja.md#mecab-ipadic-neologd-%E3%82%92%E3%82%A4%E3%83%B3%E3%82%B9%E3%83%88%E3%83%BC%E3%83%AB%E3%81%99%E3%82%8B%E6%BA%96%E5%82%99)

### その他

- [第四回 | MeCab #Python - Qiita](https://qiita.com/venect_qiita/items/5123b266478c4796db02#1-mecab%E3%81%AE%E3%82%A4%E3%83%B3%E3%82%B9%E3%83%88%E3%83%BC%E3%83%AB)
- [MeCab (めかぶ)とは？日本語の形態素解析をPythonでやってみた](https://www.internetacademy.jp/it/programming/programming-basic/what_is_mecab.html)
- [Ubuntu 20.04 LTSにMeCab(mecab-ipadic-neologd)/CaboChaのインストール #Python - Qiita](https://qiita.com/kado_u/items/e736600f8d295afb8bd9#mecab%E3%81%AE%E3%82%A4%E3%83%B3%E3%82%B9%E3%83%88%E3%83%BC%E3%83%AB)
- [【2023年版】python環境で利用できる日本語形態素解析ライブラリを比較してみた #Python - Qiita](https://qiita.com/e10persona/items/fddc795e70a05f3bc907)
- [MeCab (めかぶ)とは？日本語の形態素解析をPythonでやってみた](https://www.internetacademy.jp/it/programming/programming-basic/what_is_mecab.html)
- [第四回 | MeCab #Python - Qiita](https://qiita.com/venect_qiita/items/5123b266478c4796db02#1-mecab%E3%81%AE%E3%82%A4%E3%83%B3%E3%82%B9%E3%83%88%E3%83%BC%E3%83%AB)

### 自然言語以外の日本語処理（正規表現）

- [[総集編] Pythonで日本語の正規表現チェックをする #日本語入力 - Qiita](https://qiita.com/tikaranimaru/items/a2e85ae66bf75e16f74f)

