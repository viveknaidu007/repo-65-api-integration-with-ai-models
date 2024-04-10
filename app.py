from flask import Flask, request, jsonify
from textblob import TextBlob
import psycopg2

# Initialize Flask app
app = Flask(__name__)

# Database connection parameters
DB_HOST = 'localhost'
DB_NAME = 'sentiment_db'
DB_USER = 'postgres'
DB_PASSWORD = 'password'

# Function to perform sentiment analysis
def analyze_sentiment(text):
    analysis = TextBlob(text)
    if analysis.sentiment.polarity > 0:
        return 'positive'
    elif analysis.sentiment.polarity < 0:
        return 'negative'
    else:
        return 'neutral'

# API endpoint for sentiment analysis
@app.route('/', methods=['POST'])
def analyze_sentiment_api():
    data = request.get_json()
    text = data['text']
    sentiment = analyze_sentiment(text)

    # Store data in PostgreSQL database
    try:
        conn = psycopg2.connect(host=DB_HOST, database=DB_NAME, user=DB_USER, password=DB_PASSWORD)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO sentiments (text, sentiment) VALUES (%s, %s)", (text, sentiment))
        conn.commit()
        cursor.close()
        conn.close()
    except Exception as e:
        return jsonify({'error': str(e)}), 500

    return jsonify({'sentiment': sentiment})

if __name__ == '__main__':
    app.run(debug=True)
