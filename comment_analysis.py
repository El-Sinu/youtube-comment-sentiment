import csv
from csv import DictReader
from textblob import TextBlob 

#filename = 'Comments_Latino_MidYear_Translated.csv'
filename = 'comments_copy.csv'
#column_name = 'translated'
column_name = 'Comment'

#This Works
with open(filename, 'r', encoding='ISO-8859-1') as csvfile:
    csv_dict_reader = DictReader(csvfile)
    for row in csv_dict_reader:
        #Iterate over specific columns by column name or column number (index??)
        processed_text = TextBlob(row[column_name])
        polarity = processed_text.polarity
        print(polarity)
