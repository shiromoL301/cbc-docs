from jinja2 import Template, Environment, FileSystemLoader

from src.render import render
from src.find_docs import get_all_docs

env = Environment(loader=FileSystemLoader("./templates"))


def write_docs(body: str, path: str) -> None:
    with open(f"docs/{path}", "w") as f:
        f.write(body)


def main():
    docs = get_all_docs(DEBUG=False)

    # ==========
    # create a home page
    template = env.get_template("home.html.j2")
    home_html = template.render(docs=docs)
    write_docs(home_html, "index.html")

    # ==========
    # create doc pages
    template = env.get_template("docs.html.j2")
    for doc in docs:
        doc_html = template.render(
            body=render(doc["path"].split(".")[0]), docs=docs, **doc)
        write_docs(doc_html, doc["path"])


if __name__ == "__main__":
    main()
