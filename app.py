from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/project/<name>')
def project(name):
    return render_template('project.html', project_name=name)

@app.route('/project/neurotech')
def project_neurotech():
    return render_template('project.html', project_name='NeuroTech AI')

@app.route('/project/xo')
def project_xo():
    return render_template('project.html', project_name='XO Game AI')

@app.route('/project/weather')
def project_weather():
    return render_template('project.html', project_name='Weather App')

@app.route('/project/todo')
def project_todo():
    return render_template('project.html', project_name='To-Do List')

@app.route('/project/chatbot')
def project_chatbot():
    return render_template('project.html', project_name='ChatBot GPT')

@app.route('/project/shortener')
def project_shortener():
    return render_template('project.html', project_name='URL Shortener')

@app.route('/project/classifier')
def project_classifier():
    return render_template('project.html', project_name='Image Classifier')

@app.route('/project/password')
def project_password():
    return render_template('project.html', project_name='Password Generator')

@app.route('/project/cms')
def project_cms():
    return render_template('project.html', project_name='Portfolio CMS')

@app.route('/project/stocks')
def project_stocks():
    return render_template('project.html', project_name='Stock Price Tracker')

if __name__ == '__main__':
    app.run(debug=True)