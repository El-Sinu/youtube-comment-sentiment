import csv
from csv import DictReader
from textblob import TextBlob 


filename = 'comments_copy.csv'
column_name = 'Comment'

#This Works
with open(filename, 'r', encoding='ISO-8859-1') as csvfile:
    csv_dict_reader = DictReader(csvfile)

    with open('sentiment_scores.txt','w') as f:
        for row in csv_dict_reader:
            #Iterate over specific columns by column name or column number (index??)
            processed_text = TextBlob(row[column_name])
            polarity = processed_text.polarity
            f.write(f"{(polarity)}\n")