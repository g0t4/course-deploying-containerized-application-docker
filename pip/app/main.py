from flask import Flask, render_template

app = Flask(__name__, template_folder="../templates", static_folder="../static")

@app.route("/adder/<string:a>/<string:b>")
def adder(a, b):
    a_float = float(a)
    b_float = float(b)
    return a_float + b_float

@app.route("/")
def home():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=False)
