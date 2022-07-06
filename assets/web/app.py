from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/new-test")
def new_test():
    return render_template('new-test.html')


if __name__ == "__main__":
    app.run(debug=True)
