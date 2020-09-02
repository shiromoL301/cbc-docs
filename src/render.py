from markdown import markdown
from markdown import extensions

extensions = [
    'pymdownx.arithmatex', 'pymdownx.magiclink', 'pymdownx.highlight'
]


def render(path: str) -> str:
    text = ""
    with open(f"./md/{path}.md", mode="r") as f:
        text = f.read()

    return markdown(text, extensions=extensions)
