from flask import Flask, render_template

from src.render import render


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html.j2")


@app.route("/docs/<docs_name>")
def docs(docs_name):
    return render_template("docs.html.j2", body=render(docs_name), title="docs")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port="8080")
