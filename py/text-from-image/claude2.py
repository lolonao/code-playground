import cv2
import numpy as np
import pytesseract
from PIL import Image

def preprocess_image(image_path):
    # 画像を読み込み
    img = cv2.imread(image_path)

    # グレースケール化
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # ノイズ除去
    denoised = cv2.fastNlMeansDenoising(gray, None, 10, 7, 21)

    # 二値化（適応的閾値処理）
    binary = cv2.adaptiveThreshold(denoised, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

    # コントラスト強調
    enhanced = cv2.equalizeHist(binary)

    return enhanced

# 画像ファイルのパス
image_path = './images/001.png'

# 画像の前処理
preprocessed_img = preprocess_image(image_path)

# OCRを実行してテキストを抽出
text = pytesseract.image_to_string(preprocessed_img, lang='jpn', config='--psm 6')

# 抽出されたテキストを表示
print(text)

# 前処理後の画像を保存（確認用）
cv2.imwrite('preprocessed_image.png', preprocessed_img)
