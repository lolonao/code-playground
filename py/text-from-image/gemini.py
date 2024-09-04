import pytesseract
from PIL import Image

# Tesseract-OCRの実行パスを設定（環境に合わせて変更）
pytesseract.pytesseract.tesseract_cmd = r'/usr/bin/tesseract'

# 読み込む画像のパスを指定
img_path = 'resized_001.png'  # 画像ファイル名に合わせて変更

# 画像を読み込む
img = Image.open(img_path)

# 画像からテキストを抽出
text = pytesseract.image_to_string(img, lang='jpn')  # 日本語のOCRに設定

# 抽出されたテキストを表示
print(text)
