import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import collections
from konlpy.tag import Okt
import matplotlib as mpl
from matplotlib import font_manager, rc

fontpath = './Jalnan.ttf'
font_name = font_manager.FontProperties(fname=fontpath).get_name()
rc('font', family=font_name)
mpl.font_manager._rebuild() # 한글제목

df = pd.read_csv('./crawling/data_concat_finish/one_sentence_review_Hospital.csv', index_col=0)
df.dropna(inplace=True)
print(df.info())

print(df.head())

"""
categories = ['가정의학과', '내과', '마취통증의학과', '비뇨기과', '산부인과', '성형외과', '소아과',
              '신경과', '신경외과', '안과', '영상의학과', '외과', '이비인후과', '재활의학과',
              '정신건강의학과', '정형외과', '치과', '피부과', '한의원']
"""

hospital_index = df[df['category'] == '가정의학과'].index[0]  # hospital_index = df[df['names'] == 'Hospital_name'].index[0]
# print(movie_index)
print(df.reviews[hospital_index])  # df.cleaned_senetences[movie_index]
words = df.reviews[hospital_index].split(' ') # 띄어쓰기 기준으로 단어를 잘라서 문자열로 반환함 / df.cleaned_senetences[movie_index]
print(words)

worddict = collections.Counter(words) # 나온 단어의 빈도수를 나타냄
worddict = dict(worddict)
print(worddict)

#stopwords = ['관객', '작품', '영화', '감독', '주인공', '출연', '개봉', '촬영']

wordcloud_img = WordCloud(background_color='white', max_words=2000, font_path=fontpath).generate(df.reviews[hospital_index]) # , stopwords=stopwords
# wordcloud_img = WordCloud(background_color='white', max_words=2000, font_path=fontpath).generate_from_frequencies(worddict)

plt.figure(figsize=(8,8))
plt.imshow(wordcloud_img, interpolation='bilinear')
plt.axis('off')
plt.title(df.category[hospital_index], size=25)
plt.show()