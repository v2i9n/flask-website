from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    projects = [
        {
            'name': 'Grade Analyzer',
            'desc': 'برنامج تحليل درجات الطلاب بـ Python',
            'tech': 'Python + Pandas',
            'link': 'https://github.com/v2i9n/grade-analyzer',
            'emoji': '📊'
        },
        {
            'name': 'Grade Chart',
            'desc': 'تحويل البيانات لرسوم بيانية ملونة',
            'tech': 'Matplotlib',
            'link': 'https://github.com/v2i9n/grade-chart',
            'emoji': '📈'
        },
        {
            'name': 'XO Game AI',
            'desc': 'لعبة XO ضد ذكاء اصطناعي لا يخسر',
            'tech': 'Minimax Algorithm',
            'link': 'https://github.com/v2i9n/xo-game',
            'emoji': '🎮'
        },
        {
            'name': 'Password Generator',
            'desc': 'مولد كلمات سر قوية مع واجهة رسومية',
            'tech': 'Tkinter + Security',
            'link': 'https://github.com/v2i9n/password-generator',
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
            'link': 'https://github.com/v2i9n/voice-assistant',
            'emoji': '🎙️'
        }
    ]
    return render_template('index.html', projects=projects, name="Hussein")

if __name__ == '__main__':
    app.run(debug=True)
