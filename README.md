# CBC Docs

Code-Based Cryptography のドキュメント

[概要と進捗状況](https://github.com/shiromoL301/cbc-docs/issues/2)

# 環境構築

記事を閲覧 or 執筆するには、`Python`環境が必要になります。

## 1. Python の仮想環境を構築する(**一回目のみ**)

色々ありますが、今回は`venv`を紹介します。

まず、`venv`という名前の仮想環境を構築します。

```
python -m venv venv
```

## 2. 仮想環境に入る

`venv`という名前の仮想環境を作ったのでそこに入ります。

```
source ./venv/bin/activate
```

## 3. 必要なライブラリをインストールする(**一回目のみ**)

`requirements.txt`に必要なライブラリがあるので、それをインストールします。

```
python -m pip install -r requirements.txt
```

## 4. サーバーを起動する

```
python dev.py
```

これで、サーバーが起動します。`http://localhost:8080`で確認できます。

# 執筆

上の手順でサーバーが起動したら、執筆していきましょう。

`./md/`以下にマークダウンの作成やドキュメントの登録をしていくことになります。

> note
>
> **基本的には**この`./md/`以下のファイルしか触りません。

## 1. Markdown を書く

`./md/`内でマークダウンのファイルを作成します。今回は`./md/example.md`とします。

```Markdown
これはマークダウンの例です。必ず**削除**してください。

# チャプター

ここでは例として$1$を二回足したらどうなるかについて考えてみましょう。

## セクション

試してみた。

$$
  1 + 1 = 2
$$
```

## 2. 登録する。

ファイルを作成したら、`manifest.json`にドキュメントを登録しましょう。

```json
{
  "docs": [
    {
      "title": "マークダウンの例",
      "path": "example",
      "date": "2020/09/03",
      "author": "YAMADA TAROU"
    },
    // ...(略)...
  ]
}
```

> note
>
> `path`には必ずファイル名と同じ文字を入力してください。
