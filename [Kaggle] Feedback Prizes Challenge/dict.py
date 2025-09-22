import re
import os
import json
import nltk
import pandas as pd
from nltk.tokenize import word_tokenize
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.corpus import stopwords

def clean_text(text):
    lem = WordNetLemmatizer()
    stop_words = stopwords.words("english")

    text = text.replace(".", "")
    #replace date
    text = re.sub(r"\d{1,2}(-|/)\d{1,2}(-|/)\d{1,4}", " <date> ", text)
    #replace article tiltle, author, etc...
    text = re.sub(r"\"([a-zA-Z0-9\s.,()':!?/-])+\"", " <article> ", text)
    #replace price
    text = re.sub(r"\$([0-9,])+", " <price> ", text)
    #replace number
    text = re.sub(r"([0-9\.])+", " <nbr> ", text)
    #replace link
    text = re.sub(r'http\S+', "<URL>", text)
    text = re.sub('\&', " and ", text)

    text = re.sub("\'s", " ", text)
    text = re.sub(" whats ", " what is ", text, flags=re.IGNORECASE)
    text = re.sub("\'ve", " have ", text)
    text = re.sub("can't", "can not", text)
    text = re.sub("n't", " not ", text)
    text = re.sub("i'm", "i am", text, flags=re.IGNORECASE)
    text = re.sub("\'re", " are ", text)
    text = re.sub("\'d", " would ", text)
    text = re.sub("\'ll", " will ", text)
    text = re.sub("e\.g\.", " eg ", text, flags=re.IGNORECASE)
    text = re.sub("b\.g\.", " bg ", text, flags=re.IGNORECASE)
    
    text = text.replace("%", " percent ")
    text = text.replace("(", " <open> ")
    text = text.replace(")", " <close> ")
    text = text.replace("?", " <qtag> ")
    text = text.replace("\n"," ")
    text = text.replace("/", " / ")
    text = text.replace(",", "")
    text = text.replace(";", "")
    text = text.replace("'", "")
    text = text.replace("!", "")
    text = text.replace(":", "")
    text = text.replace("[", "")
    text = text.replace("]", "")
    text = text.replace("_", " ")
    text = text.replace("*", "")
    text = text.replace("-", " ")
    text = text.replace("\"", "")
    text = text.replace("|", "")
    text = text.lower()
    
    text_list = [lem.lemmatize(i) for i in word_tokenize(text) if not i in stop_words and len(i)>2 ]
    text = " ".join(text_list)

    return text

dirs = os.listdir("train")
dictionary = set()
for i,dir in enumerate(dirs):
    with open("train/"+ dir) as file:
        text = file.read()
        # text_list = list(text)
        # text_list = [i.lower() for i in text_list if (i!="\n" and i!="," and i!='.')]
        # text = "".join(text_list)
        text = clean_text(text)
        dict = set(word_tokenize(text))
        dictionary = dictionary.union(dict)
        print(f"File {i}")
        
       
with open("dict.json", "w") as json_file:
    json.dump({index:word for index,word in enumerate(dictionary)}, json_file, sort_keys=True, indent=4)
