from textblob import TextBlob

def analyze_sentiment(text):
    testimonial = TextBlob(text)
    return testimonial.sentiment

if __name__ == "__main__":
    text = input("Enter text for sentiment analysis: ")
    sentiment = analyze_sentiment(text)
    print(f"Sentiment Analysis: Polarity={sentiment.polarity}, Subjectivity={sentiment.subjectivity}")

