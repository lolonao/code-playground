import urllib.parse

# URLをエンコード
encoded_url = "https%3A%2F%2Fsearch.rakuten.co.jp%2Fsearch%2Fmall%2FAIBO"

# URLをデコード
decoded_url = urllib.parse.unquote(encoded_url)

# デコードされたURLを表示
print(decoded_url)

