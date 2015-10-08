import requests

from bs4 import BeautifulSoup

target_url = "http://pacpac.ru/category/arduino/offset"

def bucky_trade_spider(max_pages):

    page = 0

    while page <= max_pages:

        url = "http://pacpac.ru/category/arduino/offset"   #  + str (page * 20)
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text)

        for x in soup.findAll("a"):
            web_address = "http://pacpac.ru" + x.get("href")
            print(web_address)


        page += 1

bucky_trade_spider(0)





