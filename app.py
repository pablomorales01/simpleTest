
from flask import Flask, render_template, request
from app_lib import greeting

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    name = request.form.get("name", "")
    message = greeting(name) if name else greeting("World")
    return render_template("index.html", message=message)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
