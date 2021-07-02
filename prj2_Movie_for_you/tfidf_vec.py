import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from scipy.io import mmwrite, mmread #입출력 관련
import pickle

df_reveiw_one_senteneces = pd.read_csv('./crawling/one_sentence_review_2016_2021.csv',index_col=0)
print(df_reveiw_one_senteneces.info())

Tfidf = TfidfVectorizer(sublinear_tf=True)
Tfidf_matrix = Tfidf.fit_transform(df_reveiw_one_senteneces['reviews'])

#피클로 저장
with open('./models/tfidf.pickle','wb') as f :
    pickle.dump(Tfidf, f)

mmwrite('./models/tfidf_movie_review.mtx', Tfidf_matrix)
