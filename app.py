import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def main():
    return render_template('index.html')

@app.route("/hello/<name>")
def hello(name):
    return render_template('page.html', name=name)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="8080")
