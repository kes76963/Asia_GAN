
#crawling은 각자 진행하고 빨리 완성되는 코드로 연도를 나눠서 진행
#우선 2019년 개봉작 크롤링, 나머지는 연도별로 크롤링
#데이터는 데이터프레임으로 작업 후 저장 형식은 csv
#컬렴 명은 ['years','titles','reviews']로 통일
#파일명은 'reviews_0000.csv'로 만들기 / 0000은 연도
#크롤링 파일은 https://url.kr/rjbvyg 에 업로드

from selenium import webdriver
import pandas as pd
from selenium.common.exceptions import NoSuchElementException  # <- 그런 element가 없어도 진행하는 모듈
import time

# 크롬 드라이버 옵션 지정
options = webdriver.ChromeOptions()
#options.add_argument('headless')
options.add_argument('disable_gpu')
options.add_argument('lang=ko_KR')

# 제작연도
driver = webdriver.Chrome('chromedriver', options=options)
# years = [] # 몇 년도 작품인지 넣기 위한 빈 리스트
titles = []
reviews = []

# https://movie.naver.com/movie/sdb/browsing/bmovie.nhn?open=2019
# https://movie.naver.com/movie/sdb/browsing/bmovie.nhn?open=2019&page=1
# https://movie.naver.com/movie/sdb/browsing/bmovie.nhn?open=2019&page=2
# https://movie.naver.com/movie/sdb/browsing/bmovie.nhn?open=2019&page=3
# https://movie.naver.com/movie/sdb/browsing/bmovie.nhn?open=2020&page=2

# //*[@id="old_content"]/ul/li[1]/a
# //*[@id="old_content"]/ul/li[2]/a
# //*[@id="old_content"]/ul/li[10]/a
# //*[@id="old_content"]/ul/li[20]/a

# url = 'https://movie.naver.com/movie/sdb/browsing/bmovie.nhn?open=2019&page=43'
# driver.get(url)
# y = driver.find_elements_by_xpath('//*[@id="old_content"]/ul/li')
# print(len(y))
# driver.find_element_by_xpath('//*[@id="old_content"]/ul/li[1]/a').click() # 문자열 format
# time.sleep(0.5)
# driver.find_element_by_xpath('//*[@id="movieEndTabMenu"]/li[6]/a/em').click()

# 2019년도 개봉영화 1-43 페이지 크롤링
try:
     for i in range(1,44): # 연도별 개봉영화 리스트 페이지 수 확인하세요.
         url = 'https://movie.naver.com/movie/sdb/browsing/bmovie.nhn?open=2019&page={}'.format(i)
         # time.sleep(1)
         # 한 페이지 안에 있는 최대 20개 영화목록 크롤링
         # y = driver.find_elements_by_xpath('//*[@id="old_content"]/ul/li') # 영화 갯수
         for j in range(1,21): # 한 페이지 당 영화제목 리스트 20개
             try:
                 driver.get(url)
                 time.sleep(1)
                 movie_title_xpath = '//*[@id="old_content"]/ul/li[{}]/a'.format(j)
                 title = driver.find_element_by_xpath(movie_title_xpath).text
                 print(title)
                 driver.find_element_by_xpath(movie_title_xpath).click() # 문자열 format / 영화제목 클릭
                 time.sleep(1)
                 try:
                     btn_review_xpath = '//*[@id="movieEndTabMenu"]/li[6]/a/em'
                     driver.find_element_by_xpath(btn_review_xpath).click()  # 리뷰버튼 제목
                     time.sleep(1)
                     review_len_xpath = '//*[@id="reviewTab"]/div/div/div[2]/span/em'
                     review_len = driver.find_element_by_xpath(review_len_xpath).text
                     # print(review_len)

                     review_len = int(review_len)
                     try:
                         for k in range(1,((review_len-1) // 10)+2): # 리뷰 페이지 갯수 ((review_len-1) // 10)+2
                             review_page_xpath = '//*[@id="pagerTagAnchor{}"]/span'.format(k)
                             driver.find_element_by_xpath(review_page_xpath).click() # 리뷰 페이지 클릭
                             time.sleep(1)
                             for l in range(1,11):  # 한 페이지 당 리뷰제목 리스트 10개
                                 review_title_xpath = '//*[@id="reviewTab"]/div/div/ul/li[{}]'.format(l)
                                 try:
                                     driver.find_element_by_xpath(review_title_xpath).click()
                                     time.sleep(1)
                                     try:
                                         review_xpath = '//*[@id="content"]/div[1]/div[4]/div[1]/div[4]'
                                         review = driver.find_element_by_xpath(review_xpath).text
                                         titles.append(title)
                                         reviews.append(review)
                                         driver.back()
                                         time.sleep(1)
                                     except:
                                         driver.back()
                                         time.sleep(1)
                                         print('review crawling error')
                                 except:
                                     time.sleep(1)
                                     print('review title click error')
                     except:
                         print('review page btn click error')
                 except:
                     print('review btn click error')

             except NoSuchElementException:  # error가 발생할 경우 해당 문구를 띄운다.
                 driver.get(url)
                 time.sleep(1)
                 print('NoSuchElementException')
         print(len(reviews))
     df_review = pd.DataFrame({'titles':titles, 'reviews':reviews})
     df_review['years'] = 2019
     print(df_review.head(20))
     df_review.to_csv('./reviews_2019.csv')

except:
    print('except1')
finally:
    driver.close()












