from flask import Flask, render_template, request, session, jsonify
import random

app = Flask(__name__)
app.secret_key = 'BAD_SECRET_KEY'

newWords = ['each', 'every', 'doctor', 'patient', 'hospital', 'medicine', 'surgery', 'nurse', 'health', 'how', 'bowl', 'butter', 'butterfly', 'butterflies', 'integer', 'hour', 'time', 'second', 'minute']
seenWords = []
score = [0]

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/start', methods=["GET", "POST"])
def start():
    request.method == "POST"
    if 1 == 1:
        session['score'] = score
        session['life'] = 3
        session['word'] = random.choice(newWords)
        session['score'] = 0
        return render_template("game.html", word=session['word'], score=session['score'])
    else:
        return render_template("index.html")

@app.route('/seen', methods=["POST"])
def seen():
    result = {}
    if session['word'] in seenWords:
        session['score'] = session['score'] + 1
        session['word'] = random.choice(newWords)
        result = {'word': session['word'], 'score': session['score']}
    else:
        if session['life'] > 1:
            session['life'] = session['life'] - 1
            seenWords.append(session['word'])
            session['word'] = random.choice(newWords)
            result = {'word': session['word'], 'score': session['score']}
        else:
            result = {'gameover': True, 'score': session['score']}
    return jsonify(result)

@app.route('/new', methods=["POST"])
def new():
    result = {}
    if session['word'] in seenWords:
        if session['life'] > 1:
            session['life'] = session['life'] - 1
            session['word'] = random.choice(newWords)
            result = {'word': session['word'], 'score': session['score']}
        else:
            result = {'gameover': True, 'score': session['score']}
    else:
        seenWords.append(session['word'])
        session['score'] = session['score'] + 1
        session['word'] = random.choice(newWords)
        result = {'word': session['word'], 'score': session['score']}
    return jsonify(result)

@app.route('/gameover', methods=["GET"])
def gameover():
    score = request.args.get('score', '0')
    return render_template("gameover.html", score=score)

app.run(host='0.0.0.0', port=81)
