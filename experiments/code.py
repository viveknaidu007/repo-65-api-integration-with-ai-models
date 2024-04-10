from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Initialize the sentiment analyzer
sid = SentimentIntensityAnalyzer()

# Function to perform sentiment analysis
def analyze_sentiment(text):
    # Perform sentiment analysis
    sentiment_scores = sid.polarity_scores(text)

    # Determine the sentiment based on the compound score
    if sentiment_scores['compound'] >= 0.05:
        return 'positive'
    elif sentiment_scores['compound'] <= -0.05:
        return 'negative'
    else:
        return 'neutral'

# Input text from the user
text = input("hi buddy enter your text : ")

# Perform sentiment analysis
sentiment = analyze_sentiment(text)
print("Sentiment:", sentiment)
