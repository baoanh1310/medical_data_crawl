from scrapy.spiders import CrawlSpider
import random
from crawl_medical_data.import_setting import *
from bs4 import BeautifulSoup as soup
from scrapy import Request, FormRequest
import logging
import json

class DrugBankVNSpider(CrawlSpider):
    name = "drugbankvn_spider"
    def __init__(self, **kwargs):
        super(DrugBankVNSpider, self).__init__(**kwargs)
        self.allowed_domains = ['drugbank.vn/']
        self.start_urls =  ['https://drugbank.vn/']
        settings['CRAWLER_COLLECTION'] = 'DRUGBANK'


    def start_requests(self):
        for url in self.start_urls:
            yield Request(url, callback=self.parse)

    def parse(self , response):
        print("Response url: " + response.url)
        item_per_page = 20
        # for page_index in range(1,50):
        yield Request('https://drugbank.vn/services/drugbank/api/public/thuoc?page=7&size=20&isHide=Yes&sort=tenThuoc,asc&sort=id',
                          method='GET',
                          callback=self.parse_medical_listing,
                          # body='',
                          headers={
                              "accept": "application/json, text/plain, */*",
                              "user-agent":  random.choice(settings.get('USER_AGENT_LIST')),
                              "accept-language": 'vi,en-US;q=0.9,en;q=0.8',
                              'Content-Type': 'text/plain',
                              # 'cookie': '_ga=GA1.2.1036407420.1609982404; _gid=GA1.2.2106446813.1609982404; _gat_gtag_UA_151740144_1=1; _gat=1; _gat_gtag_UA_144904010_1=1'
                          })


    def parse_medical_listing(self, response):
        print("Response text: " + response.url)
        print("------------------------------------")
        # medical_details =  json.loads(response.body)
        #
        # # for i in range(len(medical_details)):
        # #     item ={}
        #
        #
        logging.info(response.url)
        yield {'url': response.url}
