from flask import Flask, render_template

app = Flask(__name__)

projects = [
    {
        'name': 'NeuroTech AI',
        'desc': 'نظام ذكي لقراءة إشارات الدماغ',
        'tech': 'Python + EEG + ML',
        'link': 'https://github.com/v2i9n/NeuroTech',
        'emoji': '🧠'
    },
    {
        'name': 'XO Game AI',
        'desc': 'اصطناعي لا يخسر لعبة XO',
        'tech': 'Minimax Algorithm',
        'link': 'https://github.com/v2i9n/xo-ai',
        'emoji': '🎮'
    },
    {
        'name': 'Password Generator',
        'desc': 'مولد كلمات سر قوية مع واجهة رسومية',
        'tech': 'Tkinter + Security',
        'link': 'https://github.com/v2i9n/pass-gen',
        'emoji': '🔐'
    },
    {
        'name': 'Snake Game',
        'desc': 'لعبة الثعبان الكلاسيكية',
        'tech': 'Pygame',
        'link': 'https://github.com/v2i9n/snake-game',
        'emoji': '🐍'
    },
    {
        'name': 'Voice Assistant',
        'desc': 'مساعد صوتي شخصي ينفذ الأوامر',
        'tech': 'SpeechRecognition + AI',
        'link': 'https://github.com/v2i9n/voice-bot',
        'emoji': '🎙️'
    }
]

@app.route('/')
def home():
    return render_template('index.html', projects=projects)

if __name__ == '__main__':
    app.run(debug=True)