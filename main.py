from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import random
import csv
from DetailExtractor import DetailsData
from scrapy.http import HtmlResponse
import undetected_chromedriver as uc
import time

import time
# list input this function read input_list csv return list ISBN no.
def list_input():
    lst=[]
    with open('input_list.csv', "r") as file:
        reader = csv.reader(file)
        for row in reader:
            lst.append(row[0])
    return lst[1:]

# main function in this function handling browser and using undetected_chromedriver-bypass some of  most sophisticated anti-bot mechanisms.
def data_extractor(data):
    # driver = webdriver.Chrome()
    # time.sleep(4)
    driver = uc.Chrome()
    # driver.get('https://www.booktopia.com.au/')
    # Search url taken directly passing ISBN no.
    driver.get(f'https://www.booktopia.com.au/the-screwtape-letters-letters-from-a-senior-to-a-junior-devil-c-s-lewis/book/{data}.html')
    time.sleep(5)
    # undetected_chromedriver bypass some of  most sophisticated anti-bot mechanisms
    response = HtmlResponse(url='https://www.example.com', body=driver.page_source.encode('utf-8'))
    time.sleep(5)

    # extraction data- using scrapy HtmlResponse
    a = DetailsData("booktopia_table")
    a.extract_data(response)

    driver.close()


if __name__ == '__main__':
    input_list = list_input()
    for isbn in range(len(input_list)):
        time.sleep(2)
        data=input_list[isbn]
        data_extractor(data)

    # we run also using ThreadPoolExecutor.

    # with ThreadPoolExecutor(max_workers=2) as exe:
    #     exe.map(data_extractor, input_list)

