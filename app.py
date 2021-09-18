from flask import Flask
from flask.helpers import url_for

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, world!"

app.run(port=5000)

