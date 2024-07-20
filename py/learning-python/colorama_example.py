"""参考情報
[Colorama：Pythonでコンソール出力をカラフルにするライブラリ | よくわかるpythonとエクセルVBA入門](https://python-vba.com/colorama/)
"""

from colorama import init, Fore, Back, Style

# Coloramaの初期化
init()

# 色付きテキストの出力
print(Fore.RED + 'これは赤色のテキストです。')
print(Fore.GREEN + 'これは緑色のテキストです。')
print(Fore.BLUE + 'これは青色のテキストです。')

# 背景色の変更
print(Back.YELLOW + 'これは黄色の背景を持つテキストです。' + Style.RESET_ALL)
print(Back.CYAN + 'これはシアンの背景を持つテキストです。' + Style.RESET_ALL)

# スタイルの変更
print(Style.DIM + 'これは暗いテキストです。' + Style.RESET_ALL)
print(Style.BRIGHT + 'これは明るいテキストです。' + Style.RESET_ALL)
