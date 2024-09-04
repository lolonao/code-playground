import pytesseract
from PIL import Image

# 画像ファイルのパス
image_path = './images/001.png'

# 画像を開く
img = Image.open(image_path)

# OCRを実行してテキストを抽出
text = pytesseract.image_to_string(img, lang='jpn')

# 抽出されたテキストを表示
print(text)
