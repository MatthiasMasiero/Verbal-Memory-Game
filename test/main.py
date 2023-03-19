from flask import Flask, render_template, request, session
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
   if 1==1 :
    session['score'] = score
    session['life'] = 3
    session['word'] = random.choice(newWords)
    session['score'] = 0
    return render_template("game.html", word=session['word'], score=session['score'])
   else:
    return render_template("index.html")

   
@app.route('/seen', methods=["GET", "POST"])
def seen():
  request.method == "POST"
  if session['word'] in seenWords:
    session['score'] = session['score'] + 1
    session['word'] = random.choice(newWords)
    return render_template("game.html", word=session['word'], score=session['score'])
  else:
    if session['life'] > 1:
      session['life'] = session['life'] - 1
      seenWords.append(session['word'])
      session['word'] = random.choice(newWords)
      print("not in seen")
      return render_template("game.html", word=session['word'], score=session['score'])
    else:
        return render_template("gameover.html", score=session['score'])


@app.route('/new', methods=["GET", "POST"])
def new():
  request.method == "POST"
  if session['word'] in seenWords:
    if session['life'] > 1:
      session['life'] = session['life'] - 1
      session['word'] = random.choice(newWords)
      print("in seen")
      return render_template("game.html", word=session['word'], score=session['score'])
    else:
        return render_template("gameover.html", score=session['score'])
  else:
    seenWords.append(session['word'])
    session['score'] = session['score'] + 1
    session['word'] = random.choice(newWords)
    return render_template("game.html", word=session['word'], score=session['score'])
  
@app.route('/gameover', methods=["GET"])
def gameover():
    return render_template("gameover.html", score=session['score'])
  
@app.route('/newgame', methods=["GET", "POST"])
def newgame():
  return render_template("index.html")

app.run(host='0.0.0.0', port=81)
