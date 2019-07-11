import selenium
from selenium import webdriver
import datetime
import csv
import os
import time
import argparse
import common.sources as ut

def str2bool(v):
    if isinstance(v, bool):
       return v
    if v.lower() in ('yes', 'true', 'True', 't', 'y', '1'):
        return True
    elif v.lower() in ('no', 'false', 'False', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('--company', nargs='?',  type=str, help='company to search for')
parser.add_argument('--output_data', nargs='?',  type=str, help='where do you want your files to go?', required=True)
parser.add_argument("--scrape_news", type=str2bool, nargs='?', const=True, default=False, help="if news True if stocks False")
parser.add_argument('--headless', nargs='?',  type=str2bool, default=False, help='run headless browser')

args = parser.parse_args()

output = r'..\output_data'   

if not os.path.exists(output):
    os.mkdir(output)

#company = argv[1]
options = webdriver.ChromeOptions()

if args.headless:
    options.add_argument('headless')

#options.add_argument(r"user-data-dir=C:\Users\amber\AppData\Local\Google\Chrome\User Data\Default");

driver = webdriver.Chrome(executable_path='../drivers/chromedriver.exe', chrome_options=options)
#,chrome_options=options)

if args.scrape_news: 
    filename = output + '\\' + args.company + datetime.datetime.now().strftime("%Y%m%d%H%M") + '.csv'
else:
    filename = output + '\\stock_news_' + datetime.datetime.now().strftime("%Y%m%d%H%M") + '.csv'

    if args.scrape_news:
        ut.scrape_yahoo_news(driver, filename, args.company, 1000)
    else:
        ut.scrape_stock_data(driver, filename, 1000)

    time.sleep(4)
