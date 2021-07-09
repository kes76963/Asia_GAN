import pandas as pd
import re

df_review = pd.read_csv('./model_data_Hospital_and_info2.csv',index_col=0)
df_review.info()

# a = df_review[df_review.addresses == '서울']
# print(a)
add_list = []
for i in df_review.addresses :
    a = i.split(' ')[0]
    add_list.append(a)
print(type(a))
#print(add_list)
a = df_review[df_review.names == '서울배내과의원'].iloc[0,3]
b = df_review[df_review.names == '서울배내과의원'].iloc[0,4]
c = df_review[df_review.names == '서울배내과의원'].iloc[0,5]

a = a.split(',')[:10]
a = ', '.join(a)
print(a)

# recommend = '주요 진료 과목 : {0} 주소 : {1} 전화번호 : {2}'.format(a, b, c)
# print(recommend)
#df_review.to_csv('./model_data_Hospital_and_info2.csv')


# #주소 통일
# add_dic = {'강원도' : '강원','경기도':'경기','경상남도':'경남','경상북도':'경북','광주광역시':'광주','대구광역시':'대구','대전광역시': '대전',
#            '부산광역시': '부산', '서울시' :'서울','서울특별시':'서울','서초구':'서울시 서초구','수원시':'경기','인천광역시':'인천','전라북도':'전북','제주특별자치도':'제주','충청북도':'충북'}
# add_list = list(add_dic)
#
# list = []
# for i in df_review.addresses :
#     a = i.split(' ')
#     if a[0] in add_list :
#         a[0] = add_dic[a[0]]
#     #print(a)
#     a = ' '.join(a)
#     list.append(a)
# df_review.addresses = list
# print(df_review.addresses.head(100))
# df_review.to_csv('./model_data_Hospital_and_info2.csv')

# 처음 문장 가져오기
# add_list = []
# for i in df_review.addresses :
#     a = i.split(' ')[0]
#     add_list.append(a)
#
# add_set = set(add_list)
# address = list(add_set)
# address = sorted(address)
# address.pop(0)
# print(address)





# #a/ b concat
# a = pd.read_csv('./total_reviews_Hospital_and_info2.csv',index_col=0)
# a= a.iloc[:,3:7]
# a.info()
#
# b = pd.read_csv('./model_data_Hospital_and_info.csv',index_col=0)
# b.info()
# c = pd.concat([b,a],axis=1)
#
# c.info()
# c = c.to_csv('./model_data_Hospital_and_info2.csv')



# # 치과가 포함된  2번째 열 추출
# c = c[c.category =='치과'].iloc[:9,2]
# print(c)




# #모든 열 리스트로 만들기
# total = ''
# for c in df.clinics :
#     total += c
#
# totals = total.split(', ')
# print(totals)








# #행 수정
# import pandas as pd
# import re
# df = pd.read_csv('./total_reviews_Hospital_and_info.csv',index_col=0)
# df.info()
#
# #print(df.clinics.head())
#
# # titles = list(df.clinics)
# # print(titles[:50])
# # titles = list(df.names)
# # print(titles[:50])
#
# list = []
# for c in df.clinics :
#     c = c.replace("'",'').replace('[',"").replace(']','')
#     if not c :
#         c = '없음'
#     list.append(c)
#
# df.clinics = list
# df.info()
# df.to_csv('./total_reviews_Hospital_and_info2.csv',encoding='utf-8')