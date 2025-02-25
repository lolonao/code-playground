# code-playground

様々プログラミング言語での実験場（自分用）


- [Basic usage | Documentation | Poetry - Python dependency management and packaging made easy](https://python-poetry.org/docs/basic-usage/)

- [【Vscode】過去のリリースで知らなかったかもしれない新機能のまとめ #VSCode - Qiita](https://qiita.com/Notta_Engineering/items/59fcee7f9c7e0605d3d2)

## .vscodeの内容

```json
{
    "editor.fontFamily": "'Droid Sans Mono','Noto Sans Mono CJK JP','monospace'",
    "editor.guides.indentation": false,
    "breadcrumbs.showNumbers": true,
    "editor.codeActionWidget.showHeaders": true,
    "editor.hover.sticky": true,
    "editor.minimap.enabled": false,
    "editor.lineNumbers": "off",
}
```


Vimコマンド1. カーソル位置のファイルパスを、カレントウインドウに開く

```
gf
```

このコマンドでカーソル配下にあるパスのファイルをカレントウインドウに開きます。

パスがディレクトリであった場合は、そのパスで Netrw または 設定しているファイラプラグインが開かれます。

Vimコマンド2. 水平分割した新規ウインドウに開く

```
Ctrl-w f
```

Vimコマンド3. 垂直分割した新規ウインドウに開く
```
（ノーマルモード）
:vertical wincmd f 
:vert wincmd f （上の略記）

```

## 環境

- [pipx](https://pipx.pypa.io/stable/)
- [Introduction | Documentation | Poetry - Python dependency management and packaging made easy](https://python-poetry.org/docs/)
- [SQLModel](https://sqlmodel.tiangolo.com/)
