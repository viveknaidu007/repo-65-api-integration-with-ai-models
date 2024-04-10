from flask import Flask, request, jsonify
from nltk.sentiment.vader import SentimentIntensityAnalyzer

app = Flask(__name__)

# Initialize the sentiment analyzer
sid = SentimentIntensityAnalyzer()

# Define the API endpoint for sentiment analysis
@app.route('/sentiment', methods=['POST'])
def analyze_sentiment():
    # Get the text data from the request
    text_data = request.json.get('text')

    # Perform sentiment analysis
    sentiment_scores = sid.polarity_scores(text_data)

    # Determine the sentiment based on the compound score
    if sentiment_scores['compound'] >= 0.05:
        sentiment = 'positive'
    elif sentiment_scores['compound'] <= -0.05:
        sentiment = 'negative'
    else:
        sentiment = 'neutral'

    # Prepare the response
    response = {
        'text': text_data,
        'sentiment': sentiment
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
