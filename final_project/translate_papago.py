import numpy as np
import time
import pandas as pd
from selenium import webdriver
from multiprocessing import Pool


def crawler(listname, startindex, endindex):

    # HTML selector 선택
    chromedriver = "./chromedriver.exe"
    # 크롬 드라이버 옵션 설정
    options = webdriver.ChromeOptions()

    options.add_argument("--ignore-certificate-errors")
    options.add_argument("--ignore-ssl-errors")
    # options.add_argument("--headless")
    options.add_argument("disable_gpu")
    options.add_argument("lang=ko_KR")

    driver = webdriver.Chrome(chromedriver, options=options)
    driver.implicitly_wait(10)

    driver.get("https://papago.naver.com")

    input_box = driver.find_element_by_css_selector("textarea#txtSource")
    button = driver.find_element_by_css_selector("button#btnTranslate")
    x_button = driver.find_element_by_class_name("btn_text_clse___1Bp8a")

    # translate = []
    # for text in listname[startindex:endindex]:
    #     try:
    #         input_box.clear()
    #         input_box.send_keys(text)
    #         button.click()
    #         time.sleep(3)
    #         result = driver.find_element_by_css_selector("div#txtTarget").text
    #         translate.append(result)
    #
    #         x_button.click()
    #         time.sleep(2)
    #
    #     except Exception as e:
    #         print(e)
    #
    # df_koslogan = pd.DataFrame(translate, columns=["company"])
    # driver.close()
    # return df_koslogan

    for text in listname[startindex:endindex]:
        translate = []
        try:
            input_box.clear()
            input_box.send_keys(text)
            button.click()
            time.sleep(3)
            result = driver.find_element_by_css_selector("div#txtTarget").text
            translate.append(result)
            x_button.click()
            time.sleep(2)

        except Exception as e:
            print(e)

    df = pd.DataFrame(translate, columns=["company"])
    df.to_csv(f'./datasets/Ko_slogan_{startindex}_{endindex}')
    driver.close()


if __name__ == "__main__":
    df = pd.read_csv("./datasets/slogans.csv", encoding="UTF-8")
    company_list = df["company"].tolist()
    slogan_list = df["slogan"].tolist()

    processes = 3
    rows = 5  # 불러온 파일 행수
    rows_step = np.linspace(0, rows + 1, processes + 1, dtype=int)
    iterable = [[company_list, rows_step[i], rows_step[i - 1]] for i in range(processes)]
    # pool = Pool(processes=processes)
    # results = pool.starmap(crawler, iterable)
    # pool.close()
    # pool.join()
    # df_concat = pd.concat(results, ignore_index=True)
    # df_concat.to_csv("./datasets/ko_slogan.csv", index=False)
    # print(df_concat)
    # print("Done!")
    pool = Pool(processes=processes)
    pool.starmap(crawler, iterable)
    pool.close()
    print('Done!')