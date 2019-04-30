import tweepy
import pygal
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'this site will host twitter stats'


if __name__ == '__main__':
    app.run(debug=True)
