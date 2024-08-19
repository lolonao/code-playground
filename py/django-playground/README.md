# django-playground


- [[2024 年に Django プロジェクトを本番環境向けにセットアップする方法 - Willem's Fizzy Logic](https://fizzylogic.nl/2024/03/29/how-to-set-up-a-django-project-for-production-in-2024)]


```
rye init --virtual
```

これにより、ルート パッケージ ディレクトリなしで新しいプロジェクトが初期化されます。Rye は通常どおり使用できます。Django プロジェクトの場合は、次のコマンドを実行して Django パッケージを追加できます。

```
rye add django
rye sync
```

最初のコマンドは、最新の Django パッケージを解決し、それをプロジェクト マニフェストに追加します。2 番目のコマンドは、適切な Python バージョンをダウンロードし、Django プロジェクトをプロジェクト仮想環境に同期します。

新しいDjangoプロジェクトの設定

仮想環境を使用する Python プロジェクトを開始するには、もう少し作業が必要です。新しい Django Web プロジェクトを作成するには、次のコマンドを実行して Linux/Mac でプロジェクト環境をアクティブ化します。

```
source .venv/bin/activate
```

次のコマンドを実行して新しいプロジェクトを開始できます。

```
django-admin startproject mywebsite .
```

このコマンドは、新しい Django Web プロジェクトに必要なプロジェクト ファイルを現在のディレクトリに追加します。次のコマンドを使用して、Web サイトを実行できるようになりました。

```
python manage.py migrate
python manage.py runserver
```

最初のコマンドは、データベースを最新バージョンに移行します。 2 番目のコマンドは、Web サーバーを起動して、Web サイトを で利用できるようにします。 この Web サイトはまだ本番環境の準備ができていません。

さまざまな環境の設定を管理する

前のセクションでは、新しい Django プロジェクトを開始する方法について説明しました。 mywebsite前のセクションの指示に従った場合、設定は という名前のパッケージに保存されます。設定のバージョンは 1 つだけですが、テストと本番では異なる設定の組み合わせが必要になります。




