import pandas as pd
from gensim.models import Word2Vec

review_word = pd.read_csv('./crawling/cleaned_review_2017_2021.csv',index_col=0)
print(review_word.info())
cleaned_token_review = list(review_word['cleaned_reviews'])
#print(len(cleaned_token_review))
cleaned_tokens = []
count = 0
for sentence in cleaned_token_review :
    token = sentence.split(' ')
    cleaned_tokens.append(token)
#print(len(cleaned_tokens))
#print(cleaned_token_review[0])
#print(cleaned_tokens[0]) #형태소 형태로 바꿈

embedding_model = Word2Vec(cleaned_tokens, vector_size=100, window=4, min_count=20, workers=4,
                           #vector_size 차원수 / window 4 커널 사이즈 / min_count 출연빈도 / workers cpu 몇개 사용하는지
                           epochs=100, sg=1) #몇 번 학습 / 어떤 알고리즘
embedding_model.save('./models/word2VecModel_2016_2021.model')
#print(embedding_model.wv.vocab.keys())
#print(len(embedding_model.wv.vocab.keys())) #단어 사전에 단어가 몇개 있는지
