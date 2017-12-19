#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/main.html")
def hello():
    return render_template('main.html')

@app.route("/login.html")
def login():
    return render_template('login.html')

if __name__ == "__main__":
    app.run(debug=True)

print
