import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import json


# Need to un-comment out to update the library if starting this code in a new enviorment.
nltk.download('averaged_perceptron_tagger')
nltk.download('vader_lexicon')

#data = []
#for line in open('pranaj.json', 'r'):
    #data.append(json.loads(line))

# open json file that is in the same directory
with open('metaphorsFound.json') as f:
    # load json data into a python object
    data = json.load(f)


# loop through 'tweets' looking for certin keys
for tweets in data['tweets']:
    #print(tweets['like count'], tweets['url'])
    #del tweets['metaphorFamily']
    #del tweets['date']
    #del tweets['url']
    #del tweets['like count']
    del tweets['tags']
    #del tweets['retweets']
    #del tweets['metaphorFamily']
    #del tweets['null']



# Sentiment analyze
sent = SentimentIntensityAnalyzer()

for tweet in data['tweets']:
    analyze = sent.polarity_scores(tweet['review'])

    #print(int but is a float, convert to float.)
    tweet['SentimentScore'] = analyze['compound']

    # Compound: compound > 0: Positive Sentiment.   c < 0: Negative.   c == 0: Neutral.
    #print(analyze['compound'])

    if analyze['compound'] > 0:
        print('Positive')
        tweet['Sentiment'] = "Positive"
        tweet['SentimentScore'] = analyze['compound']
    elif analyze['compound'] < 0:
        print('Negative')
        tweet['Sentiment'] = "Negative"
        tweet['SentimentScore'] = analyze['compound']
    elif analyze['compound'] == 0:
        print('Neutral')
        tweet['Sentiment'] = "Neutral"
        tweet['SentimentScore'] = analyze['compound']




with open('DataSentimentAnalyzed.json', 'w') as f:
    json.dump(data, f, indent = 2)
