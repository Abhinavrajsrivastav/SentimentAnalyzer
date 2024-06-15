from textblob import TextBlob

def analyze_sentiment(text):
    blob = TextBlob(text)
    sentiment_score = blob.sentiment.polarity

    if sentiment_score > 0:
        return "Positive"
    elif sentiment_score < 0:
        return "Negative"
    else:
        return "Neutral"

def main():
    print("Welcome to Sentiment Analyzer!")
    text = input("Enter a sentence or phrase: ")
    sentiment = analyze_sentiment(text)
    print(f"Sentiment: {sentiment}")

if __name__ == "__main__":
    main()
