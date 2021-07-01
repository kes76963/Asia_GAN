import pandas as pd
from konlpy.tag import Okt
import re

df = pd.read_csv('/content/crawling/reviews_2019_part.csv', index_col=0)
print(df.head())

okt = Okt()

stopwords = pd.read_csv('/content/crawling/stopwords.csv', index_col= 0)

movie_stopwords = ['영화','배우','감독']
stopwords_list = list(stopwords.stopword) + movie_stopwords

count = 0
cleaned_sentences = []
for sentence in df.reviews :
  count += 1
  if count % 10 == 0 :
    print('.', end='')
  if count % 100 == 0 :
    print('') #줄바꿈
  sentence = re.sub('[^가-힣 | ' ']','',sentence)
  token = okt.pos(sentence, stem = True) #stem true로 하면 원형으로 바꿔줌
  df_token = pd.DataFrame(token, columns=['word','class'])
  df_cleaned_token = df_token[(df_token['class'] =='Noun') |
                            (df_token['class'] == 'Verb') |
                            (df_token['class'] == 'Adjective')]
  words = []
  for word in df_cleaned_token['word'] :
    if len(word) >1 :
      if word not in stopwords_list :
        words.append(word)
  cleaned_sentence = ' '.join(words)       
  cleaned_sentences.append(cleaned_sentence)
df['cleaned_sentences'] = cleaned_sentences
print(df.head())

df.info()

df = df[['titles','cleaned_sentences']]
print(df.info())
df.to_csv('./cleaned_review_2019_part.csv')