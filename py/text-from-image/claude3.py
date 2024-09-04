import cv2
import numpy as np
import pytesseract
from PIL import Image

def preprocess_image(image_path):
    # 画像を読み込み
    img = cv2.imread(image_path)
    # 画像の解像度を上げる（元の画像が低解像度の場合）：
    img = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)


    # グレースケール化
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # 軽度のぼかしを適用（ノイズ軽減）
    blurred = cv2.GaussianBlur(gray, (3, 3), 0)

    # 軽度のシャープニング
    sharpened = cv2.addWeighted(gray, 1.5, blurred, -0.5, 0)

    # 軽度のコントラスト調整
    alpha = 1.2  # コントラスト制御（1.0-3.0）
    beta = 10    # 明るさ制御（0-100）
    adjusted = cv2.convertScaleAbs(sharpened, alpha=alpha, beta=beta)

    return adjusted

# 画像ファイルのパス
image_path = './images/001.png'

# 画像の前処理
preprocessed_img = preprocess_image(image_path)

# OCRを実行してテキストを抽出
# custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'
custom_config = r'--oem 3 --psm 4 -c preserve_interword_spaces=1'
# text = pytesseract.image_to_string(preprocessed_img, lang='jpn+eng', config=custom_config)

# 元の画像をそのまま使用する（前処理なし）：
text = pytesseract.image_to_string(Image.open(image_path), lang='jpn+eng', config=custom_config)

# 抽出されたテキストを表示
print(text)

# 前処理後の画像を保存（確認用）
cv2.imwrite('preprocessed_image.png', preprocessed_img)
