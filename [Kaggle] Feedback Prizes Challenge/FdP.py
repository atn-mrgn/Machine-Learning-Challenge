import keras
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.model_selection import train_test_split
from keras.preprocessing.text import Tokenizer
from clean_text import clean_text


train_df = pd.read_csv("train.csv")
copy_train_df = train_df.copy()
copy_train_df.drop(["id", "discourse_id", "discourse_start", "discourse_end", "discourse_type_num", "predictionstring"], axis=1, inplace=True)

# redac = list(copy_train_df.discourse_text)

# vectorizer = CountVectorizer()
# vector = vectorizer.fit_transform(redac)

copy_train_df.discourse_text = copy_train_df.discourse_text.apply(clean_text)

tk = Tokenizer(num_words=None, filters='!"#$%&()*+,-./:;=?@[\\]^_`{|}~\t\n')

tk.fit_on_texts(copy_train_df.discourse_text)

print(tk.document_count)

print(list(tk.word_counts.items())[:10])

print(len(list(tk.word_counts.items())))

print(sorted(list(tk.word_counts.items()), key= lambda x: -x[1])[:10])


