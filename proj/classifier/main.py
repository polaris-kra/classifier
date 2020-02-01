from flask import render_template
from classifier.server import ClassifierServer


server = ClassifierServer()
app = server.create()


@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    server.run()
