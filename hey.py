import tweepy
import time


# Authenticate to Twitter


API_KEY="MQIvJyPotAsSCVB7SlU8L5QHM"
API_SECRET="zui2nPE7nb1zXnLlkoFhzxNaQQzft4D3ZGDzNnPtkzLlkvsvx0"
ACCESS_SECRET="kGwusNPETQEaDgUgQGqRigaJ08U1S8FmNAcGjeSleiMKg"
ACCESS_TOKEN="1221127314857168896-XEfIcAoEXIMQbnuNgmFm73Om4kLpTT"



auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

api = tweepy.API(auth, wait_on_rate_limit=True,
    wait_on_rate_limit_notify=True)

# list
def like(id):
    try:
        api.create_favorite(id)
    except Exception as ex:
        print(ex)

# Create API object

class MyStreamListener(tweepy.StreamListener):
    def __init__(self, api):
        self.replied_tweets = []
        self.api = api

    def on_status(self, status):
        print("==========================================================")
        
        follow_id=(status.user.id)
        message="Hi what's up"
        tweet_id=status.id
        if tweet_id in self.replied_tweets:
            print("already seen this tweet: ", status.text)
        else:
            
            time.sleep(60*5)
            self.api.retweet(tweet_id)
            
            print("==========================================================")
            self.replied_tweets.append(tweet_id)
        
        if len(self.replied_tweets) >= 1000:
            self.replied_tweets = []
    

if __name__ == "__main__":
    tweets_listener = MyStreamListener(api)
    stream = tweepy.Stream(api.auth, tweets_listener)
    print("streaming...")
    stream.filter(track=['#onlyfans'])
    print("after stream...")
