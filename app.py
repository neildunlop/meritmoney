from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    """Display a simple hello world message when the index is hit."""
    return "Hello Tom!"


if __name__ == '__main__':
    app.run(debug=True)
