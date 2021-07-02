import pandas as pd
from sklearn.metrics.pairwise import linear_kernel
from scipy.io import mmwrite, mmread
import pickle

df_review_one_sentence = pd.read_csv('./crawling/one_sentence_review_2016_2021.csv',index_col=0)

# #pandas 개념 정리
# print(df_review_one_sentence.iloc[0]) # 타이틀, 리뷰 다나옴
# print(df_review_one_sentence.iloc[0,1]) #0번 컬럼, 0번 로우 / 요소 1개 뽑기 - reveiw 나옴
# print(df_review_one_sentence.iloc[0:5,0]) # 제목 5개
# print(df_review_one_sentence.loc[:, 'titles']) #컬럼명으로 보겠다 / 제목만 출력
# print(df_review_one_sentence['titles'][0]) #타이틀에 0
# df.iloc[row,col] 숫자로
# df.loc['Tom','math'] 컬럼명으로
# exit()

ls = ['겨울왕국','라이온킹','알라딘']
print(list(enumerate(ls))) #튜플 리스트로 보여줌 / [(0, '겨울왕국'), (1, '라이온킹'), (2, '알라딘')]
for idx,i in enumerate(ls) : #0 겨울왕국, 1 라이온킹, 2 알라딘 출력 / 인덱스 값 같이 보여줌
    print(idx, i)

for idx, i in enumerate(ls):
    if i == '라이온킹':
        print(idx)

ls = ['겨울왕국','라이온킹','알라딘']
리스트 = [아이 + '짱 재밌당' for 아이 in ls]  #['겨울왕국짱 재밌당', '라이온킹짱 재밌당', '알라딘짱 재밌당']
print(리스트)

exit()


Tfidf_matrix = mmread('./models/tfidf_movie_review.mtx').tocsr()
with open('./models/tfidf.pickle','rb') as f :
    Tfidf = pickle.load(f)

def getRecommendation(cosine_sin) :
    simScore = list(enumerate(cosine_sin[-1])) #어떤게 어떤 영화의 유사도 갖는지 알기 위해서 enumerate /
    simScore = sorted(simScore, key=lambda  x:x[1], reverse=True) #큰 순으로
    simScore = simScore[1:11] #0번은 자기 자신
    movieidx = [i[0]for i in simScore] # i 에는 (0, '겨울왕국') 이렇게 들어있음 / 튜플 중에 0번 인덱스 뽑겠다
    recMovieList = df_review_one_sentence.iloc[movieidx]
    return  recMovieList

movie_idx = df_review_one_sentence[df_review_one_sentence['titles']=='존 윅 3: 파라벨룸 (John Wick: Chapter 3 - Parabellum)'].index[0]
#movie_idx = 130  # 번호로 했을 때
print(df_review_one_sentence.iloc[movie_idx,0])

cosine_sin = linear_kernel(Tfidf_matrix[movie_idx], Tfidf_matrix) #특정값(idx)와 모든 영화 코사인 유사도 구해서
recommendation = getRecommendation(cosine_sin)
print(recommendation)
#print(recommendation.iloc[0]) 제목만 보고 싶을 때