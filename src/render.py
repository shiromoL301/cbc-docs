from markdown import Markdown
from markdown import extensions
from pymdownx import superfences

extensions = [
    'pymdownx.arithmatex',
    'pymdownx.b64',
    'pymdownx.magiclink',
    'pymdownx.details',
    'pymdownx.extra',
    'pymdownx.superfences',
    'pymdownx.highlight'
]

extension_configs = {
    "pymdownx.magiclink": {
        "repo_url_shortener": True,
        "repo_url_shorthand": True,
        "provider": "github",
        "user": "facelessuser",
        "repo": "pymdown-extensions"
    },
    "pymdownx.superfences": {
        "custom_fences": [
            {
                'name': 'mermaid',
                'class': 'mermaid',
                'format': superfences.fence_div_format
            }
        ]
    }
}


def render(path: str) -> str:
    text = ""
    with open(f"./md/{path}.md", mode="r") as f:
        text = f.read()

    md = Markdown(extensions=extensions, extension_configs=extension_configs)
    return md.convert(text)
