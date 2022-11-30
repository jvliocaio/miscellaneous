import tweepy, json, os, sys
from dotenv import load_dotenv

load_dotenv('./.env')

consumer_key = os.getenv('API_KEY')
consumer_secret = os.getenv('API_SECRET_KEY')
access_token = os.getenv('ACCESS_TOKEN')
access_token_secret = os.getenv('ACCESS_TOKEN_SECRET')
bearer_token = os.getenv('BEARER_TOKEN')

api = tweepy.Client(
    consumer_key=consumer_key,
    consumer_secret=consumer_secret,
    access_token=access_token,
    access_token_secret=access_token_secret,
    bearer_token=bearer_token
)

def tweetar():
    msg = "Tinha que estar programando pra ficar rico logo"

    try:
        tweet = api.create_tweet(text=msg)
        print(tweet)
    except tweepy.TweepyException as e:
        print(e)

def get_tweets():
    response = api.search_recent_tweets("nelson de sá", max_results=100)
    tweets = response.data
    for tweet in tweets:
        print(tweet.text)

def options():
    opt = sys.argv[1]
    match opt:
        case "twt":
            tweetar()
        case "gtwt":
            get_tweets()
        case "PHP":
            print("You can become a backend developer")
        case "Solidity":
            print("You can become a Blockchain developer")
        case "Java":
            print("You can become a mobile app developer")
        case _:
            print("The language doesn't matter, what matters is solving problems.")

options()
