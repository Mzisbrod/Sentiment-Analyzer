from flask import Flask, render_template, request
from sentiment_analyzer import analyze_sentiment

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        text = request.form['text']
        sentiment = analyze_sentiment(text)
        return render_template('index.html', polarity=sentiment.polarity,
                               subjectivity=sentiment.subjectivity, text=text)
    else:
        return render_template('index.html', polarity=None, subjectivity=None, text='')

if __name__ == '__main__':
    app.run(debug=True)