from flask import Flask
from time import time

app = Flask("app")


@app.route("/")
def home():
    return f"Hello, Flask! [{time()}]"
