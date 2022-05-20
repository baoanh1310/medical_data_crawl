from scrapy.spiders import CrawlSpider
import random
from crawl_medical_data.import_setting import *
from bs4 import BeautifulSoup as soup
from scrapy import Request, FormRequest
import logging
import json

class CongKhaiYTeSpider(CrawlSpider):
    name = "congkhaiyte_spider"
    def __init__(self, **kwargs):
        super(CongKhaiYTeSpider, self).__init__(**kwargs)
        self.allowed_domains = ['congkhaiyte.moh.gov.vn']
        self.start_url =  ['https://congkhaiyte.moh.gov.vn/']
        settings['CRAWLER_COLLECTION'] = 'CONGKHAIYTE'


    def start_requests(self):
        for url in self.start_url:
            yield Request(url, callback=self.parse)

    def parse(self , response):
        item_per_page = 30
        for page_index in range(1,int(62438/item_per_page) + 1):
            yield FormRequest('https://congkhaiyte.moh.gov.vn/?module=Content.Listing&moduleId=10&cmd=redraw&site=2001869&url_mode=rewrite&submitFormId=10&moduleId=10&page=Project.MedicalPrice.Home.MedicalPrice.Drug.list&site=2001869',
                              method='POST',
                              callback=self.parse_medical_listing,
                              body= "layout=Project.MedicalPrice.Home.MedicalPrice.Drug.list&itemsPerPage={}&pageNo={}&service=Project.MedicalPrice.Home.MedicalPrice.Drug.selectAll&widgetCode=Multimedia&type=MedicalPrice.Drug&page=Project.MedicalPrice.Home.MedicalPrice.Drug.list&modulePosition=3&moduleParentId=-1&groupId=&menuId=&orderBy=&phpModuleName=Content.Listing&_t=1609770494638".format( item_per_page,page_index),
                              headers={
                                  "Content-Type": "application/x-www-form-urlencoded",
                                  "User-Agent":  random.choice(settings.get('USER_AGENT_LIST')),
                                  "Accept-Language": 'vi,en-US;q=0.9,en;q=0.8'
                              })


    def parse_medical_listing(self, response):
        s = soup(response.text, features='lxml').table

        for tr in  s.findAll("tr"):
            item = {}
            for i, td in enumerate(tr.find_all('td')):
                if i == 1:
                    item['medication_name'] = td.text.split('Xem chi tiết')[1].strip()
                elif i == 2:
                    item['active_ingredient'] = td.text
                elif i == 5:
                    item['packaging'] = td.text
                elif i == 6:
                    item['unit'] = td.text
                elif i == 9:
                    item['distributor'] = td.text
                elif i == 10:
                    item['price'] = td.text

            logging.info(json.dumps(item))
            yield  item