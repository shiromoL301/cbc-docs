from jinja2 import Template, Environment
from markdown import markdown 

options = {
    'page-size': 'A4',
    'margin-top': '0.1in',
    'margin-right': '0.1in',
    'margin-bottom': '0.1in',
    'margin-left': '0.1in',
    'encoding': "UTF-8",
    'no-outline': None
}


if __name__ == "__main__":
    body_row_text = """
# Hello World

```
def main():
    return "hi"
```

$h$

$$
x + y = z
$$
$$
E(\mathbf{v}, \mathbf{h}) = -\sum_{i,j}w_{ij}v_i h_j - \sum_i b_i v_i - \sum_j c_j h_j
$$

\[3 < 4\]

\begin{align}
    p(v_i=1|\mathbf{h}) & = \sigma\left(\sum_j w_{ij}h_j + b_i\right) \\
    p(h_j=1|\mathbf{v}) & = \sigma\left(\sum_i w_{ij}v_i + c_j\right)
\end{align}
    """
    
    result = Template("""
    <html>
        <head>
        <script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
<script src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-chtml.js"></script>
        </head>
        <body>
            <h1>Hello, {{ name }}</h1>
            <article>
                {{ body }}
            </article>
        </body>
    </html>
    """).render(name = "syakoo", body = markdown(body_row_text, extensions=['pymdownx.arithmatex']))
    print(result)