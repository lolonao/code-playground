"""
[OCRの精度を高めよう！Pythonで行う画像の前処理テクニック | AI JIMY Labo.](https://aijimy.com/dx/python-ocr-technique/)
"""
import sys
import cv2

def step1() -> None:
    """
    解像度調整のコード例
    解像度を300dpiに調整するコード例です。画像の解像度が低い場合は、解像度調整でOCRの精度が向上します。
    """
    # 画像を読み込む
    image = cv2.imread('./images/001.png')

    # 現在の解像度を確認
    height, width = image.shape[:2]
    print(f'元の解像度: {width} x {height}')

    # 解像度を300dpiに調整
    new_height = int(height * (300 / 96))  # 96dpiから300dpiへ
    new_width = int(width * (300 / 96))
    resized_image = cv2.resize(image, (new_width, new_height))

    # 調整後の解像度を確認
    print(f'調整後の解像度: {new_width} x {new_height}')

    # 調整後の画像を保存
    cv2.imwrite('resized_001.png', resized_image)


def step2() -> None:
    """グレースケール化のコード例
    カラー画像をグレースケール画像に変換して、データ量を減少させ、ノイズを軽減します。"""
    # 画像を読み込む
    image = cv2.imread('resized_001.png')

    # グレースケール化
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # グレースケール画像を保存
    cv2.imwrite('gray_001.png', gray_image)

def step3() -> None:
    """ノイズ除去のコード例
    ノイズ除去によって、OCRの精度がさらに向上します。以下の例では、バイラテラルフィルタを使用してノイズを除去します。"""
    # グレースケール画像を読み込む
    gray_image = cv2.imread('gray_001.png', 0)

    # バイラテラルフィルタでノイズ除去
    denoised_image = cv2.bilateralFilter(gray_image, 9, 75, 75)

    # ノイズ除去後の画像を保存
    cv2.imwrite('denoised_001.png', denoised_image)

def step4() -> None:
    """二値化のコード例
    二値化は、画像を白黒の2色に変換し、文字と背景を明確に区別する手法です。二値化により、OCRソフトウェアが文字を認識しやすくなります。"""
    # ノイズ除去後の画像を読み込む
    denoised_image = cv2.imread('denoised_001.png', 0)

    # 大津の方法で二値化
    _, binary_image = cv2.threshold(denoised_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # 二値化した画像を保存
    cv2.imwrite('binary_image.png', binary_image)


if __name__ == "__main__":
    step1()
    # step2()
    # step3()
    # step4()
