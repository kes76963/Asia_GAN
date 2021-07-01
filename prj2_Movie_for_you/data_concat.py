import pandas as pd

# #중복제거 / 원래는 크롤링 후에 했어야 했음
# df_dup = pd.read_csv('./crawling/cleaned_review_2020.csv',index_col =0)
#
# df_undup = df_dup.drop_duplicates()
# print(df_undup.duplicated().sum())
# df_undup.to_csv('./crawling/cleaned_review_2020.csv')

df = pd.read_csv('./crawling/one_sentence_reveiw_2017.csv', index_col=0)
#df2 = pd.read_csv('./crawling/cleaned_review_2020 (1).csv', index_col=0)

print(df.info())
df_dup.drop_duplicates()
df.dropna(inplace=True)
print(df.info())

df.columns['titles','cleaned_reviews']

for i in range(18,22) :
    df_temp = pd.read_csv(f'./crawling/one_sentence_reveiw_20{i}.csv')
    df_dup.drop_duplicates()
    df_temp.dropna(inplace=True)
    df_temp.columns['titles', 'cleaned_reviews']
    df = pd.concat([df, df_temp],ignore_index=True)

print(df.info())
df.to_csv('./crawling/movie_review_2017_2020')


