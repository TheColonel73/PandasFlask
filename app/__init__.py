from flask import Flask, render_template, request
from werkzeug.serving import run_simple

import os

app = Flask(__name__)

# Replace the existing home function with the one below
@app.route("/")
def home():
    return "Hello there!" # render_template("home.html")


@app.route('/user_request', methods=['POST'])
def build_user_request():
    if request.is_json:
        data = request.json
        print(data)
    return "Done!"