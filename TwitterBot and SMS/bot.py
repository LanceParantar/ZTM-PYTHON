
import tweepy
import time
auth = tweepy.OAuthHandler('')#TOKEN
auth.set_access_token('') #YTOKEN

api = tweepy.API(auth)

user = api.me()

def limit_handle(cursor):
    try:
        while True:
            yield cursor.next()
    except tweepy.RateLimitError:
        time.sleep(1000)
        
for follower in limit_handle(tweepy.Cursor(api.followers).items()):
    print(follower.name)
