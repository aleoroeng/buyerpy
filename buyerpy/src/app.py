from flask import Flask, render_template

DEBUG = True
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, world!"
@app.route("/index")
def index():
    return render_template("main.html", name="main")

app.run(port=5000)

