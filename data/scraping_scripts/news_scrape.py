import selenium
from selenium import webdriver
import datetime
from bs4 import BeautifulSoup
from sys import argv
import csv
import os
import time
import re

#goes back a directory creates or writes to output_data
output = r'..\output_data'   

if not os.path.exists(output):
    os.mkdir(output)

patt = re.compile(r'<([A-Za-z0-9]|\/|,|;|\.|{|}|\[|\]|#|"|:|\-|_|=|%| )+>')

#company = argv[1]

#options = webdriver.ChromeOptions()
#options.add_argument(r"user-data-dir=C:\Users\amber\AppData\Local\Google\Chrome\User Data\Default");

driver = webdriver.Chrome(executable_path='../drivers/chromedriver.exe')
#,chrome_options=options)

for a in argv[1:]:
    with open(output + '\\' + a + datetime.datetime.now().strftime("%Y%m%d%H%M") + '.csv', 'w', encoding='utf8',newline='') as f:
        writer = csv.writer(f)
        for i in range(1,1011,10):
            url = (r'https://news.search.yahoo.com/search;_ylt=AwrC2Q6Zs_tcqg8AzgLQtDMD;_ylu=X3oDMTFhZDJibWJ0BGNvbG8DYmYxBHBvcwMxBHZ0aWQDQjc1MDZfMQRzZWMDcGFnaW5hdGlvbg--?p=' 
                + a + r'&fr=uh3_news_vert_gs&fr2=sb-top-news.search&b=' 
                + str(i) + r'&pz=10&bct=0&xargs=0')
            print(a + ': ' + str(i))
            #url = url_base + str(i)
            driver.get(url)
            #divs = driver.find_elements_by_xpath('//div[@class="g card"]')
            divs = driver.find_elements_by_xpath('//li[@class="ov-a fst"]')
            for d in divs:
                links = d.find_elements_by_xpath('//h4[@class="fz-16 lh-20 mah-42 ov-h"]')
                sources = d.find_elements_by_xpath('//span[@class="mr-5 cite-co"]')
                for i in range(len(links)):
                    if i < len(sources):
                        writer.writerow([patt.sub('',links[i].get_attribute("innerHTML")),patt.sub('', sources[i].get_attribute("innerHTML"))])
                    else:
                        break
            time.sleep(4)
    time.sleep(4)
