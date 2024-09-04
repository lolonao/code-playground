import cv2
import numpy as np
import pytesseract

def improve_ocr(image_path, threshold=127, kernel_size=3, psm=6, oem=3):
  """
  OCRの精度を向上させるための前処理を行う関数

  Args:
      image_path (str): 画像ファイルのパス
      threshold (int, optional): 二値化の閾値. Defaults to 127.
      kernel_size (int, optional): カーネルサイズ. Defaults to 3.
      psm (int, optional): PSMモード. Defaults to 6.
      oem (int, optional): OCRエンジンモード. Defaults to 3.

  Returns:
      str: 抽出されたテキスト
  """

  # 画像を読み込む
  img = cv2.imread(image_path)

  # グレースケール化
  gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

  # 二値化
  thresh, img_bin = cv2.threshold(gray, threshold, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

  # ノイズ除去
  kernel = np.ones((kernel_size, kernel_size), np.uint8)
  img_opening = cv2.morphologyEx(img_bin, cv2.MORPH_OPEN, kernel)

  # テキスト抽出
  config = f'--psm {psm} --oem {oem}'
  text = pytesseract.image_to_string(img_opening, config=config, lang='jpn')

  return text

# 画像のパスを指定
image_path = './images/001.png'

# パラメータを調整
threshold = 150  # 二値化の閾値
kernel_size = 5  # カーネルサイズ
psm = 7         # PSMモード

# 関数を呼び出してテキストを抽出
extracted_text = improve_ocr(image_path, threshold, kernel_size, psm)

print(extracted_text)
