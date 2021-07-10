import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import collections
from konlpy.tag import Okt
import matplotlib as mpl
from matplotlib import font_manager, rc
from konlpy.tag import Okt

# 한글 폰트 안 깨지도록 설정
fontpath = './malgun.ttf'
font_name = font_manager.FontProperties(fname=fontpath).get_name()
rc('font', family=font_name)
mpl.font_manager._rebuild()

titles = ['치과', '피부과', '성형외과', '안과', '산부인과', '비뇨기과', '정신건강의학과', '정형외과', '마취통증의학과',
              '신경외과', '재활의학과', '영상의학과', '외과', '신경과', '소아과', '내과', '이비인후과', '가정의학과', '한의원']

for i in range(0,19):
    df = pd.read_csv(f'../crawling/reviews_Hospital_{titles[i]}.csv', index_col=0)
    df.dropna(inplace=True)
    #print(df.info())

    #print(df.head(20))

    hospital_reivews = df['reviews']       #병원 리뷰
    #print(movie_index)

    words = []

    for hospital_review in hospital_reivews:
        #word = hospital_review.split(' ') # 문장을 띄어쓰기 기준으로 잘라 문자열 리스트로 반환
        okt = Okt()
        word = okt.nouns(hospital_review)
        words.append(word)

    worddict = collections.Counter(word)# 유니크한 단어를 뽑아 몇 번 나오는지 빈도 표시
    worddict = worddict.most_common(100)
    worddict = dict(worddict)
    print(worddict)
    #stopwords = ['관객', '작품', '주인공', '개봉', '촬영', '출연']

    # wordcloud_img = WordCloud(background_color = 'white', max_words = 2000,
    #                           font_path = fontpath, stopwords=stopwords).generate_from_frequencies(worddict)
    # total_review = list(df['reviews'])
    # total_review = '\n'.join(total_review)
    # print(total_review)
    wordcloud_img = WordCloud(background_color = 'white', max_words = 2000,
                              font_path = fontpath).generate(str(worddict))

    plt.figure(figsize=(8,8))
    plt.imshow(wordcloud_img, interpolation='bilinear')
    plt.axis('off')     # 눈금 끄기
    plt.title(f'{titles[i]}', size=25)
    plt.show()
    wordcloud_img.to_file(f'{titles[i]}.png')
