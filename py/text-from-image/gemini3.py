import cv2
import numpy as np
import pytesseract

def improve_ocr(image_path):
    """
    OCRの精度を向上させるための前処理を行う関数

    Args:
        image_path (str): 画像ファイルのパス

    Returns:
        str: 抽出されたテキスト
    """

    # 画像を読み込む
    img = cv2.imread(image_path)

    # グレースケール化
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # 二値化（Otsuの二値化）
    thresh, img_bin = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # ノイズ除去（開演算）
    kernel = np.ones((3, 3), np.uint8)
    img_opening = cv2.morphologyEx(img_bin, cv2.MORPH_OPEN, kernel)  # 開演算

    # テキスト抽出
    config = '--psm 6 --oem 3'  # PSMモード6、LSTMエンジン
    text = pytesseract.image_to_string(img_opening, config=config, lang='jpn')

    return text

# 画像のパスを指定
image_path = './images/001.png'

# 関数を呼び出してテキストを抽出
extracted_text = improve_ocr(image_path)

print(extracted_text)
