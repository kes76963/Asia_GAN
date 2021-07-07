import pandas as pd

categories = ['내과', '마취통증의학과', '비뇨기과', '산부인과', '성형외과', '소아과',
              '신경과', '신경외과', '안과', '영상의학과', '외과', '이비인후과', '재활의학과',
              '정신건강의학과', '정형외과', '치과', '피부과', '한의원']

# one_sentences로 concat하기
df = pd.read_csv('./crawling/one_sentence_review_가정의학과.csv', index_col=0)
# print(df.info())
df.drop_duplicates()
df.dropna(inplace=True)
print(df.info())

df.columns = ['names', 'reviews', 'category']
df.to_csv('./crawling/one_sentence_review_가정의학과.csv')

for category in categories:
    df_temp = pd.read_csv(f'./crawling/one_sentence_review_{category}.csv', index_col=0)
    df_temp.dropna(inplace=True)
    df_temp.drop_duplicates()
    df_temp.columns = ['names', 'reviews', 'category']
    #df_temp.to_csv(f'./crawling/cleaned_review_{category}.csv')
    df = pd.concat([df, df_temp],ignore_index=True)
print(df.info())
df.to_csv('./crawling/data_concat_finish/one_sentence_review_Hospital.csv')