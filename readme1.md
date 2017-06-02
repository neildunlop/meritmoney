## Our first simple API

Our first attempt simply returns 'Hello World' when we hit the root of our application  (http://localhost:5000/)

```
from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    """Display a simple hello world message when the index is hit."""
    return "Hello World!"


if __name__ == '__main__':
    app.run(debug=True)
```
