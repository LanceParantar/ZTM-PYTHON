
import tweepy
import time
auth = tweepy.OAuthHandler('RZchrxd0XJVvZpwGqzT3DmiRt', 'fc2nCjfjiddrZU54F7Wz8Yp7YxjKxQ1iGvOeefKBaX8iyvCCO3')
auth.set_access_token('747433118211022850-kGlHgDKILRd7NQRL96KPe6UuXOdEDZ1', 'HABT0UisUVak5cy4Hk8P2dhox6K0CFXEIJNy6ZPmHYbP8')

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
