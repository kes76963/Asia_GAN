import pandas as pd
import matplotlib.pyplot as plt
from gensim.models import Word2Vec
from sklearn.manifold import TSNE
from matplotlib import font_manager, rc
import matplotlib as mpl

font_path = './wordcloud/malgun.ttf'
font_name = font_manager.FontProperties(fname=font_path).get_name()
mpl.rcParams['axes.unicode_minus']=False
rc('font', family=font_name)

embedding_model = Word2Vec.load('./models/word2VecModel_hospital.model')
key_word = '정형외과'
sim_word = embedding_model.wv.most_similar(key_word, topn=10)       # 가장 유사한 10개 추출
print(sim_word)

vectors = []
labels = []
for label, _ in sim_word:
    labels.append(label)
    vectors.append(embedding_model.wv[label])
df_vectors = pd.DataFrame(vectors)
print(df_vectors.head())            # 100차원 공간 속의 좌표

tsne_model = TSNE(perplexity=40, n_components=2, init='pca', n_iter=2500, random_state=23)      # TSNE로 2차원 평면에 투시
new_values = tsne_model.fit_transform(df_vectors)
df_xy = pd.DataFrame({'words':labels, 'x':new_values[:, 0], 'y':new_values[:, 1]})
print(df_xy.head())

print(df_xy.shape)
df_xy.loc[df_xy.shape[0]] = (key_word,0, 0)
plt.figure(figsize=(8, 8))
plt.scatter(0, 0, s=1500, marker='*')       # x, y 좌표로 산점도 그리기 / marker는 마크 모양, s는 마커 사이즈

for i in range(len(df_xy.x)):
    a = df_xy.loc[[i, 10], :]
    plt.plot(a.x, a.y, '-D', linewidth=2)
    plt.annotate(df_xy.words[i], xytext=(5,2),      # xytext = 출력될 텍스트의 좌표
                  xy=(df_xy.x[i], df_xy.y[i]),      # 점의 좌표
                  textcoords='offset points',       # 약간 띄움
                  ha='right', va='bottom')      # ha = 수평 정렬, va = 수직 정렬 / va='bottom'은 글자 아래 선에 맞춰 정렬
plt.show()