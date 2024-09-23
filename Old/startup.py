from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return open("index.html")


if __name__ == '__main__':
    app.run()
