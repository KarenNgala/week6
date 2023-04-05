from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_geek():
    return '<h2>Week 6: Flask with Docker</h2>'


if __name__ == "__main__":
    app.run(debug=True)