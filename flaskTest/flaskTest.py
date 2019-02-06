from flask import Flask, render_template

import time
import pyautogui

#code from https://github.com/CoreyMSchafer

app = Flask(__name__)



@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=pyautogui.position())

@app.route("/about")
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)