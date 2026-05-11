from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/project/neurotech')
def neurotech():
    return "<h1 style='text-align:center; margin-top:100px; font-family:sans-serif'>NeuroTech AI<br><br>قريباً 🚀</h1>"

@app.route('/project/xo')
def xo():
    return "<h1 style='text-align:center; margin-top:100px; font-family:sans-serif'>XO Game AI<br><br>قريباً 🚀</h1>"