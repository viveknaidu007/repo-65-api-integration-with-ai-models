import json
from flask import Flask, render_template, request, jsonify
from nltk.sentiment.vader import SentimentIntensityAnalyzer   #VADER (Valence Aware Dictionary and sEntiment Reasoner) for sentiment analysis
import psycopg2

# initialize flask
app = Flask(__name__)

# intialize SentimentIntensityAnalyzer
sid = SentimentIntensityAnalyzer()

# functoin for calling 
def analyze_sentiment(text):
    # using polarity_scores method to get the sentiment scores
    scores = sid.polarity_scores(text)
    if scores['compound'] > 0:
        return 'positive'
    elif scores['compound'] < 0:
        return 'negative'
    else:
        return 'neutral'

# now we are defining the API endpoint for sentiment analysis
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyze_sentiment', methods=['POST'])
def analyze_sentiment_api():
    text = request.form['text']
    sentiment = analyze_sentiment(text)
    save_to_database(text, sentiment)
    return render_template('result.html', sentiment=sentiment) 

# now we are defining the  function to save data to PostgreSQL database
def save_to_database(text, sentiment):
    conn = psycopg2.connect(
        dbname="sentiment",  #give ur databsename
        user="postgres",     #give ur user
        password="12345678", #give ur password which u gave while installing 
        host="localhost",    #defaut it was 
        port="5001"          #give ur port in ur sql only or it will show error
    )
    cur = conn.cursor()
    cur.execute("INSERT INTO sentiment_data (text, sentiment) VALUES (%s, %s)", (text, sentiment))

    #for seeing our data that stored in database we can do below
    cur.execute("SELECT * FROM sentiment_data")

    # for fetching all rows from the result set
    rows = cur.fetchall()

    # for printing the data in our terminal
    for row in rows:
        print(row)


    conn.commit()
    conn.close()

if __name__ == '__main__':
    app.run(debug=True)
