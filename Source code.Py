
import tweepy
from textblob import TextBlob
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# Twitter API credentials (replace with your own)
api_key = 'YOUR_API_KEY'
api_secret = 'YOUR_API_SECRET'
access_token = 'YOUR_ACCESS_TOKEN'
access_token_secret = 'YOUR_ACCESS_TOKEN_SECRET'

# Authenticate with Twitter
auth = tweepy.OAuthHandler(api_key, api_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Function to clean and analyze sentiment
def analyze_sentiment(tweet):
    analysis = TextBlob(tweet)
    if analysis.sentiment.polarity > 0:
        return 'Positive'
    elif analysis.sentiment.polarity == 0:
        return 'Neutral'
    else:
        return 'Negative'

# Fetch tweets
query = "mental health"
tweets = tweepy.Cursor(api.search_tweets, q=query, lang="en").items(100)

sentiments = {"Positive": 0, "Neutral": 0, "Negative": 0}
all_text = ""

for tweet in tweets:
    text = tweet.text
    sentiment = analyze_sentiment(text)
    sentiments[sentiment] += 1
    all_text += " " + text

# Visualization: Pie chart
labels = sentiments.keys()
sizes = sentiments.values()
colors = ['green', 'gray', 'red']
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
plt.axis('equal')
plt.title("Sentiment Analysis of Tweets")
plt.show()

# Word cloud for tweet content
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(all_text)
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title("Word Cloud of Tweets")
plt.show()
