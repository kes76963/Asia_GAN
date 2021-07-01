import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud #패키지 이름이랑 py이름 겹치면 에러 뜰 수도 있음
import collections
from konlpy.tag import Okt
import matplotlib as mpl
from matplotlib import font_manager, rc

fontpath = './Jalnan.ttf'
font_name = font_manager.FontProperties(fname=fontpath).get_name()
rc('font', family = font_name)
mpl.font_manager._rebuild()
#df = pd.read_csv('cleaned_review_2020.csv', index_col=0)
df = pd.read_csv('one_sentence_reveiw_2020.csv', index_col=0)
df.dropna(inplace=True)
print(df.info())

print(df.head(20))
movie_index = df[df['titles'] == '100% 울프: 푸들이 될 순 없어 (100% Wolf)'].index[0]
#print(movie_index)
print(df.reviews[movie_index])
words = df.reviews[movie_index].split(' ')
print(words)

worddict = collections.Counter(words)
worddict = dict(worddict) #딕셔너리로 만들기
print(worddict)

stopwords = ['작품','관객','주인공','개봉','감독']
# wordcloud_img = WordCloud(background_color='white', max_words=2000,
#                           font_path=fontpath).generate_from_frequencies(worddict)
#stopword 처리
wordcloud_img = WordCloud(background_color='white', max_words=2000,
                          font_path=fontpath, stopwords=stopwords).generate(df.reviews[movie_index])
plt.figure(figsize=(8,8))
plt.imshow(wordcloud_img, interpolation='bilinear')
plt.axis('off')
plt.title(df.titles[movie_index],size =25)
plt.show()
