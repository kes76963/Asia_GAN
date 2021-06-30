#crawling 작업

#crawling은 각자 진행하고 빨리 완성되는 코드로 연도를 나눠서 진행
#우선 2019년 개봉작 크롤링, 나머지는 연도별로 크롤링
#데이터는 데이터프레임으로 작업 후 저장 형식은 csv
#컬렴 명은 ['year','titles','reviews']로 통일
#파일명은 'reviews_0000.csv'로 만들기 / 0000은 연도
#크롤링 파일은 https://url.kr/rjbvyg 에 업로드

#이런 식으로 사전에 통일감 있게 만들기
class crawling_naver() :
    def crawling (self, page, url) :
        pass

    def data_save (self, path) :
        pass

from selenium import webdriver
import pandas as pd
from selenium.common.exceptions import NoSuchElementException #오류가 있을 때 지나간다
import time

options = webdriver.ChromeOptions()
#options.add_argument('headless') #크롬 열리는게 안 보임
options.add_argument('disable_gpu')
options.add_argument('lang=ko_KR')

driver = webdriver.Chrome('chromedriver', options=options)
years = []
titles = []
reviews = []

# https://movie.naver.com/movie/sdb/browsing/bmovie.nhn?open=2019&page=1
#//*[@id="old_content"]/ul/li[1]/a
#//*[@id="old_content"]/ul/li[10]/a


#2019년 개봉영화 리스트
try:
    for i in range(1, 44): # 2019년 개봉영화 리스트 44
        url = f'https://movie.naver.com/movie/sdb/browsing/bmovie.nhn?open=2019&page={i}'
        time.sleep(0.5)
        for j in range(1, 21): # 영화 갯수
            try: # 제목
                driver.get(url)
                time.sleep(1)
                movie_title_xpath = f'//*[@id="old_content"]/ul/li[{j}]/a'
                title = driver.find_element_by_xpath(movie_title_xpath).text
                print(title)
                driver.find_element_by_xpath(movie_title_xpath).click()
                time.sleep(1)
                try: # 리뷰
                    btn_review_xpath = '//*[@id="movieEndTabMenu"]/li[6]/a/em'
                    driver.find_element_by_xpath(btn_review_xpath).click()  # 리뷰 버튼 클릭
                    time.sleep(1)
                    review_len_xpath = '//*[@id="reviewTab"]/div/div/div[2]/span/em' # 총 리뷰 수
                    review_len = driver.find_element_by_xpath(review_len_xpath).text

                    review_len = int(review_len) # 리뷰 길이 int 값으로
                    try:
                        for k in range(1, ((review_len-1) // 10)+2): # 리뷰 갯수로 최대 페이지 계산
                            review_page_xpath = f'//*[@id="pagerTagAnchor{k}"]/span' # 리뷰 페이지 버튼 xpath
                            driver.find_element_by_xpath(review_page_xpath).click() # 리뷰 페이지 클릭
                            time.sleep(1)
                            for l in range(1, 11): # 한 페이지에 있는 리뷰 모두 크롤링
                                review_title_xpath = f'//*[@id="reviewTab"]/div/div/ul/li[{l}]' # 리뷰 제목 xpath
                                try:
                                    driver.find_element_by_xpath(review_title_xpath).click() # 리뷰 제목 xpath 클릭
                                    time.sleep(1)
                                    try:
                                        review_xpath = '//*[@id="content"]/div[1]/div[4]/div[1]/div[4]' # 리뷰 내용 xpath
                                        review = driver.find_element_by_xpath(review_xpath).text
                                        titles.append(title)
                                        reviews.append(review)
                                        driver.back()
                                        time.sleep(1)
                                    except:
                                        driver.back()
                                        time.sleep(0.5)
                                        print('review crawling error')
                                except:
                                    time.sleep(1)
                                    print('review title click error')
                    except:
                        print('review page btn click error')
                except:
                    print('review btn click error')
            except NoSuchElementException:
                driver.get(url)
                time.sleep(1)
                print('NoSuchElementException')

        print(i,'번째 페이지 완료')

        df_review = pd.DataFrame({'titles':titles, 'reviews':reviews})
        df_review['years'] = 2019
        print(df_review.head(20))
        df_review.to_csv('./reviews_2019_{}_page.csv')
        print(i, '번째 페이지 저장 완료')
except:
    print('except1')
finally:
    driver.close()
