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


The block:

```if __name__ == '__main__':
    app.run(debug=True)
```

makes python check that the code is being executed from the main module, if it is then it should be executed in debug mode.  This allows us to reuse this code as a module if needed.
(See https://stackoverflow.com/questions/419163/what-does-if-name-main-do)
