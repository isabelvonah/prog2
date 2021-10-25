from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return '<p> Hhkajsödlfk </p>'


@app.route("/hello/<name>")
def hello(name):
    name = name.upper()
    return render_template("index.html", name=name)



if __name__ == "__main__":
    app.run(debug=True, port=5000)