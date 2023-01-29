import csv
from csv import DictReader
from textblob import TextBlob 

filename = 'comments_copy.csv'
column_name = 'Comment'

#Define Function to give sentiment scores using textblob
def sentiment(comment):
    processed_text = TextBlob(comment)
    polarity = processed_text.polarity
    return int(polarity)

final = []
comments = [
    {'Comment_ID': 0, 'Comment': 'This sucks!!'},
    {'Comment_ID': 2, 'Comment': 'Everything is wonderful'},
    {'Comment_ID': 3, 'Comment': 'This video is the best, I love it'},
    {'Comment_ID': 4, 'Comment': "Woah, I can't believe it"},
    {'Comment_ID': 5, 'Comment': "Meh, I'm indiferent about this"},
    {'Comment_ID': 6, 'Comment': 'Cool beans'},
    {'Comment_ID': 1, 'Comment': 'I hate my life'}
    ]

for i in range(len(comments)):
    comment = comments[i]
    final.append({
        'Comment_ID': comment["Comment_ID"], 
        'Comment': comment["Comment"],
        'sentiment_score': sentiment(comment["Comment"])
    })

print(final)
