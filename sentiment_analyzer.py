from textblob import TextBlob
import matplotlib.pyplot as plt
from collections import Counter

# Store sentiments
sentiments = []

def analyze_sentiment(text):
    analysis = TextBlob(text)
    polarity = analysis.sentiment.polarity

    if polarity > 0.1:
        return "Positive"
    elif polarity < -0.1:
        return "Negative"
    else:
        return "Neutral"

print("Real-Time Sentiment Analyzer")
print("Type 'exit' to stop\n")

# Simulated real-time input
while True:
    text = input("Enter Tweet/Post: ")

    if text.lower() == 'exit':
        break

    sentiment = analyze_sentiment(text)
    sentiments.append(sentiment)

    print(f"Sentiment: {sentiment}\n")

# Visualization
if sentiments:
    count = Counter(sentiments)

    labels = list(count.keys())
    values = list(count.values())

    plt.bar(labels, values)
    plt.title("Sentiment Analysis Result")
    plt.xlabel("Sentiment")
    plt.ylabel("Number of Posts")
    plt.show()
else:
    print("No data to display.")