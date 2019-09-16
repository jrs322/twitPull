#!/usr/local/bin/python3
import json
import time
from twython import Twython


class TwitPull():
    def __init__(self):
        self.credentials = self.gen_credentials()
        self.twython_inst = Twython(self.credentials['CONSUMER_KEY'],
                                    self.credentials['CONSUMER_KEY_SECRET'],
                                    self.credentials['ACCESS_TOKEN'],
                                    self.credentials['ACCESS_TOKEN_SECRET'])
        tweet = self.twython_inst.get_home_timeline(count=10, exclude_replies=True)
        filtered_tweet = self.filter_tweet(tweet)
        print(filtered_tweet)
        time.sleep(5)

    def gen_credentials(self):
        with open("twitter_credentials.json", "r") as file:
            creds = json.load(file)
        return creds

    def filter_tweet(self, tweet):
        important_data = tweet.count()
        return important_data


try_twit = TwitPull()
