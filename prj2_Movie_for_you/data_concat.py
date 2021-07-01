# 모듈 임포트
import pandas as pd

# # 중복제거
# df_dup = pd.read_csv('./crawling/cleaned_review_2017.csv', index_col=0)
# df_undup = df_dup.drop_duplicates()
# print(df_undup.duplicated().sum()) # 중복제거 확인
#
# df_undup.to_csv('./crawling/cleaned_review_2019.csv') # 중복이 0이면 저장
# exit() # 프로그램 종료

# 첫(기준) 데이터 로드
df = pd.read_csv('./crawling/one_sentence_review_2017.csv', index_col=0)
print(df.info())

df.drop_duplicates()
df.dropna(inplace=True)
print(df.info())

df_temp.columns = ['titles', 'cleaned_reviews']

for i in range(18, 21):
    df_temp = pd.read_csv(f'./crawling/one_sentence_review_20{i}.csv', index_col=0) # 이어붙일 데이터들 로드
    df_temp.dropna(inplace=True) # nan값 제거
    df_temp.drop_duplicates() # 중복 제거
    df_temp.columns = ['titles', 'cleaned_reviews'] # 컬럼명 변경
    df_temp.to_csv(f'./crawling/one_sentence_review_20{i}.csv') # 저장
    df = pd.concat([df, df_temp], ignore_index=True) # 이어붙이기
print(df.info())
df.to_csv('./crawling/one_sentence_review_2017_2020.csv')