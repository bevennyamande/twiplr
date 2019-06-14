#!/usr/bin/env python3

import tweepy
import click
from tweepy.auth import OAuthHandler

consumer_key = 'Q47knI9nZpfMzKm0fcDWd'
consumer_secret = 'S6D5lr3WbrsVB99JQhl4w1Yng4NsgvNlZtbKVSEUHDiEkOjyV0'
access_token = '63067026-FMDLfZG079PPrpzTo4LjSdjDVuSnRMaraJlccsGdd'
access_token_secret = 'bZdjj7pMnbgjc4HHy4iVAITm8WyJFjLjG8NrMqfd7urLk'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
user = api.get_user('werkzeug')

## Objective os the application
# the application should be commandline tool
# the user must input a user to enumerate and get the data
# should be a valid twitter account
# get a description about the account
# able to create a wordlist from the given data and given input
# ie enter surname to generate a wordlist based on the surname of the target
# save the output of the generated wordlist to a specified directory
