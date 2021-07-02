import pandas as pd
from sklearn.metrics.pairwise import linear_kernel
from scipy.io import mmwrite, mmread
import pickle

df_review_one_sentence = pd.read_csv('./crawling/one_sentence_review_2016_2021.csv',index_col=0)

Tfidf_matrix = mmread('./models/tfidf_movie_review.mtx').tocsr()
with open('./models/tfidf.pickle','rb') as f :
    Tfidf = pickle.load(f)

def getRecommendation(cosine_sin) :
    simScore = list(enumerate(cosine_sin[-1]))
    simScore = sorted(simScore, key=lambda  x:x[1], reverse=True)
    simScore = simScore[1:10]
    movieidx = [i[0]for i in simScore]
    recMovieList = df_review_one_sentence.iloc[movieidx]
    return  recMovieList

movie_idx = df_review_one_sentence[df_review_one_sentence['titles']=='존 윅 3: 파라벨룸 (John Wick: Chapter 3 - Parabellum)'].index[0]
#movie_idx = 130  # 번호로 했을 때
print(df_review_one_sentence.iloc[movie_idx,0])

cosine_sim = linear_kernel(Tfidf_matrix[movie_idx], Tfidf_matrix)
recommendation = getRecommendation(cosine_sim)
print(recommendation)