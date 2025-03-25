#!/usr/local/bin/python3
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

comments = [ "this is fye",
            "I like this",
]
def sentiment_analysis():
    analyzer = SentimentIntensityAnalyzer()
    for comment in comments:
        vs = analyzer.polarity_scores(comment)
        print("{:-<65} {}".format(comment, str(vs)))

sentiment_analysis()