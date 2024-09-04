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
    img_dilation = cv2.dilate(img_bin, kernel, iterations=1)
    img_erosion = cv2.erode(img_dilation, kernel, iterations=1)

    # テキスト抽出
    config = '--psm 6'  # PSMモードを6に設定（単一、長いテキスト行）
    text = pytesseract.image_to_string(img_erosion, config=config, lang='jpn')

    return text

# 画像のパスを指定
image_path = './images/001.png'

# 関数を呼び出してテキストを抽出
extracted_text = improve_ocr(image_path)

print(extracted_text)
