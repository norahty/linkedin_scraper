from flask import Flask
from flask import render_template
from flask import request
import json

from main import returnProfileInfo

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html', name="Hello World")


@app.route("/extract", methods=["POST"])
def submit():
    res = returnProfileInfo(request.form["url"])
    return render_template('output.html', result=res)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
