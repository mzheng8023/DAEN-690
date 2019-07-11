import selenium
import csv
import re

def check_for_element(driver,xpath):
    return len(driver.find_elements_by_xpath(xpath)) > 0

def scrape_yahoo_news(driver, filename, company, rng=2011, n_headlines=1000):
    patt = re.compile(r'<([^>])+>')
    count = 0
    headlines = []
    for i in range(1,rng,10):
        with open(filename, 'w', encoding='utf8',newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['headline','source','label'])
        if count >= n_headlines:
            break
        url = (r'https://news.search.yahoo.com/search;_ylt=AwrC2Q6Zs_tcqg8AzgLQtDMD;_ylu=X3oDMTFhZDJibWJ0BGNvbG8DYmYxBHBvcwMxBHZ0aWQDQjc1MDZfMQRzZWMDcGFnaW5hdGlvbg--?p=' 
            + company + r'&fr=uh3_news_vert_gs&fr2=sb-top-news.search&b=' 
            + str(i) + r'&pz=10&bct=0&xargs=0')
        print(company + ': ' + str(count))
        #url = url_base + str(i)
        driver.get(url)
        #divs = driver.find_elements_by_xpath('//div[@class="g card"]')
        divs = driver.find_elements_by_xpath('//li[@class="ov-a fst"]')
        for d in divs:
            links = d.find_elements_by_xpath('//h4[@class="fz-16 lh-20"]')
            sources = d.find_elements_by_xpath('//span[@class="mr-5 cite-co"]')
            for i in range(len(links)):
                if i < len(sources):
                    headline = patt.sub('',links[i].get_attribute("innerHTML"))
                    if headline not in headlines:
                        headlines.append(headline)
                        count +=1
                        with open(filename, 'a', encoding='utf8',newline='') as f:
                            writer = csv.writer(f)
                            writer.writerow([headline,patt.sub('', sources[i].get_attribute("innerHTML")),1])
                else:
                    break

def scrape_stock_data(driver, filename, rng=2011, n_headlines=1000):
    with open(filename, 'w', encoding='utf8',newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['headline','label'])
    patt = re.compile(r'<([^>])+>')
    url = 'https://www.nasdaq.com/news/market-headlines.aspx'
    count = 0
    headlines = []
    for i in range(1,rng):
        if i > 1:
            url = 'https://www.nasdaq.com/news/market-headlines.aspx?page='+str(i)
        driver.get(url)
        if count >= n_headlines:
            break
        articles = driver.find_elements_by_xpath('//a[contains(@id,"ArticleLink")]')
        for d in articles:
            headline = d.get_attribute("innerHTML")
            if headline not in headlines:
                headlines.append(headline)
                count +=1
                with open(filename, 'a', encoding='utf8',newline='') as f:
                    writer = csv.writer(f)
                    #default to irrelevant
                    writer.writerow([patt.sub('', headline),0])