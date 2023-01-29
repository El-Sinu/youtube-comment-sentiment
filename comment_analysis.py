import csv
from csv import DictReader
from textblob import TextBlob 

filename = 'comment_test.csv'
column_name = 'Comment'

########Define Function to give sentiment scores using textblob
def sentiment(comment):
    processed_text = TextBlob(comment)
    polarity = processed_text.polarity
    return int(polarity)
###########################################################

########## Trying to do this via reading CSV instead #########

file_handle = open(filename, "r", encoding="utf8")
csv_reader = DictReader(file_handle)
#Error: object of type 'DictReader' has no len(), because DictReader is an iterator
#convert to list instead.
# KeyError: 'Comment_ID'
comments = list(csv_reader)

final = []
for i in range(len(comments)):
    comment = comments[i]
    final.append({
        "Comment_ID": comment["Comment_ID"], 
        "Comment": comment["Comment"],
        "Polarity": sentiment(comment["Comment"])
    })

print(final)