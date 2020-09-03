from flask import Flask, render_template

from src.render import render
from src.find_docs import find_doc, get_all_docs

app = Flask(__name__)


@app.route("/")
def home():
    docs = get_all_docs()
    return render_template("home.html.j2", docs=docs)


@app.route("/docs/<docs_name>")
def docs(docs_name):
    docs = get_all_docs()
    doc = find_doc(docs_name)

    if doc is None:
        raise ValueError(
            "ドキュメントが見つかりませんでした。manifest.jsonに情報を入力し忘れている可能性があります。")

    return render_template("docs.html.j2", body=render(docs_name), docs=docs, **doc)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port="8080")
