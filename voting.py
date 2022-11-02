import datetime

from flask import Flask, request, render_template

app = Flask(__name__)

candidates = ['cat', 'dog', 'mouse']
tally = {c: 0 for c in candidates}


@app.route('/hello')
def hello():
    return 'Hello, World!'


@app.post('/vote')
def vote():
    data = request.json
    name = data.get('name', None)
    if name in candidates:
        tally[name] += 1
        return tally
    else:
        return 'Invalid Candidate', 400


@app.get('/result')
def result():
    return render_template('result.html', tally=tally, now=datetime.datetime.now())


if __name__ == '__main__':
    app.run(host='0.0.0.0', threaded=True, port=8888)
