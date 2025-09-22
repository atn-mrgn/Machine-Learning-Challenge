from copy import deepcopy
from nltk.tokenize import sent_tokenize
import re
import json

text = "Mr. John Archadius is True legend of U.S.A, but history of him is'nt good. Legend determine the price of narrative document. \"Bob flying in the world\" such as fly is good following. You are flies adjustement the 12-30-2020"

with open("dict.json") as json_file:
    dictionary = json.load(json_file)

words = list(dictionary.values())
print(words.index("<article>"))