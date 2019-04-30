import tweepy
from tweepy.auth import OAuthHandler
import pygal
from flask import Flask

consumer_key = 'Q47knI9nZpfMzKm0fcDWd'
consumer_secret = 'S6D5lr3WbrsVB99JQhl4w1Yng4NsgvNlZtbKVSEUHDiEkOjyV0'
access_token = '63067026-FMDLfZG079PPrpzTo4LjSdjDVuSnRMaraJlccsGdd'
access_token_secret = 'bZdjj7pMnbgjc4HHy4iVAITm8WyJFjLjG8NrMqfd7urLk'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
user = api.get_user('werkzeug')

app = Flask(__name__)


@app.route('/')
def index():
    return 'this site will host twitter stats'


if __name__ == '__main__':
    print(user)
    app.run(debug=True)
