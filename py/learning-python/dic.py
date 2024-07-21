"""参考情報
[ゼロからはじめるPython(52) Pythonでちょっと使えるデスクトップ英和辞書 | TECH+（テックプラス）](https://news.mynavi.jp/techplus/article/zeropython-52/)
"""
import tkinter as tk
import sqlite3

# ボタンを押したときの処理を記述 --- (*1)
def search_dic():
    # テキストボックスから英単語を得る --- (*2)
    word = textWord.get()
    # データベースへ接続する --- (*3)
    conn = sqlite3.connect("ejdict.sqlite3")
    c = conn.cursor()
    # SQLを実行して単語データを取り出す --- (*4)
    sql = '''SELECT * FROM items WHERE word LIKE ?
    ORDER BY level DESC LIMIT 10'''
    rows = c.execute(sql, (word,))
    result = ""
    for n in rows:
        result += "【{0}】{1}\n".format(n[1],n[2])
        print(n)
    conn.close()
    # 検索結果を表示 --- (*5)
    textResult.delete('1.0', 'end') #一度全部消す
    textResult.insert(tk.END, result)

# ウィンドウを作成 --- (*6)
win = tk.Tk()
win.title("英和辞書")
win.geometry("500x250")

# 部品を作成 --- (*7)
labelWord = tk.Label(win, text='英単語:')
labelWord.pack()

textWord = tk.Entry(win)
textWord.insert(tk.END, 'hello')
textWord.pack()

calcButton = tk.Button(win, text='検索')
calcButton["command"] = search_dic
calcButton.pack()

textResult = tk.Text(win)
textResult.insert(tk.END, 'ここに結果が表示されます')
textResult.pack()

# ウィンドウを動かす --- (*8)
win.mainloop()

