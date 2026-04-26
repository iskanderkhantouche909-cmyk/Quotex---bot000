from flask import Flask
import subprocess
import os
import signal

app = Flask(__name__)

# نخزن الـ process اللي يشغل boot.py
bot_process = None

@app.route('/')
def home():
    return '''
    <h1>Quotex Bot Control</h1>
    <a href="/start">▶️ Start Bot</a><br>
    <a href="/stop">⏹ Stop Bot</a>
    '''

@app.route('/start')
def start_bot():
    global bot_process
    if bot_process is None:
        bot_process = subprocess.Popen(["python", "boot.py"])
        return "✅ البوت بدا يخدم!"
    else:
        return "⚠️ البوت راهو يخدم بالفعل."

@app.route('/stop')
def stop_bot():
    global bot_process
    if bot_process is not None:
        os.kill(bot_process.pid, signal.SIGTERM)
        bot_process = None
        return "⏹ البوت توقف!"
    else:
        return "⚠️ البوت راهو متوقف أصلاً."