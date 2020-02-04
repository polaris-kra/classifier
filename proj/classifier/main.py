from PIL import Image
import numpy as np
from flask import render_template, request
from classifier.server import ClassifierServer


server = ClassifierServer()
app = server.create()


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/classify", methods=["GET", "POST"])
def classify():
    if request.method == "GET":
        return render_template("classify.html", result=None)

    result = None

    if "img" in request.files:
        image = request.files["img"]
        image = Image.open(image)
        result = server.classify(image)

    return render_template("classify.html", result=result)


@app.route("/logs")
def logs():
    start = int(request.args.get("start") or 0)
    count = int(request.args.get("count") or 0)
    count = min(count, 300)

    logs_ = [f"log_{i}" for i in range(start, start+count)]

    return render_template("logs.html", logs=logs_)


if __name__ == "__main__":
    server.run()
