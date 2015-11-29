from flask import Flask, render_template, session, request
from flask import redirect, url_for
import util
import re

app = Flask(__name__)

@app.route("/", methods = ['GET','POST'])
def index():
        return "cool"


if __name__ == "__main__":
        app.secret_key = "hello"
        app.run(host='0.0.0.0', port=8000)
