from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    html = """
<html>
  <body>
    <h1>Hello!</h1>
  </body>
</html>
"""
    return html


if __name__ == '__main__':
    app.run(debug=True)