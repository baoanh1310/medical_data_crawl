from scrapy.spiders import CrawlSpider
import random
from crawl_medical_data.config.lst_disease_group import *
from crawl_medical_data.import_setting import *
from bs4 import BeautifulSoup as soup
from scrapy import Request, FormRequest
import logging
import json

class NhaThuocAnKhangSpider(CrawlSpider):
    name = "nhathuocanhkhang_spider"
    def __init__(self, **kwargs):
        super(NhaThuocAnKhangSpider, self).__init__(**kwargs)
        self.allowed_domains = ['nhathuocankhang.com']
        self.start_url =  ['https://www.nhathuocankhang.com']
        settings['CRAWLER_COLLECTION'] = 'NHATHUOCANKHANG'


    def start_requests(self):
        for url in self.start_url:
            yield Request(url, callback=self.parse)

    def parse(self , response):
        for category_index in list(dict_disease_category.values()):
            yield FormRequest('https://www.nhathuocankhang.com/aj/Category/Products',
                              method='POST',
                              callback=self.parse_medication_intro,
                              body= "Key=&PageSize=200&PageIndex=0&Category={}".format(category_index),
                              headers={
                                  "content-type": "application/x-www-form-urlencoded",
                                  "user-agent":  random.choice(settings.get('USER_AGENT_LIST')),
                                  "accept-language": 'vi,en-US;q=0.9,en;q=0.8'
                              })


    def parse_medication_intro(self, response):
        res_text = response.text
        s = soup(res_text, features='lxml')

        total_links = list(set(s.find_all('a')))
        for link in total_links:
            link = link.get('href')
            total_link = 'https://www.nhathuocankhang.com' + link
            yield  response.follow(total_link, self.parse_medication_general)


    def parse_medication_general(self, response):
        print("URL:" + response.url)
        item = {}

        medication_name = response.xpath('/html/body/section/div[1]/aside[2]/h1').get()
        item['medication_name'] = soup(medication_name, "lxml").text

        lst_images= response.xpath('//img/@src').extract()
        try:
            item['image_link_1'] = soup(lst_images[0], "lxml").text
        except:
            pass

        try:
            item['image_link_2'] = soup(lst_images[2], "lxml").text
        except:
            pass

        try:
            medication_package = response.xpath('/html/body/section/div[1]/aside[2]/div[2]/span[1]').get()
            item['packaging'] = soup(medication_package, "lxml").text.split(':')[1]
        except:
            pass

        try:
            active_ingredient = response.xpath("/html/body/section/div[1]/aside[2]/div[2]/span[2]").get()
            item['active_ingredient'] = soup(active_ingredient, "lxml").text.split(':')[1]
        except:
            pass

        try:
            disease_group = response.xpath("/html/body/section/div[1]/aside[2]/div[2]/span[3]/a").get()
            item['disease_group'] = soup(disease_group, "lxml").text
        except:
            pass
        try:
            manufacterer = response.xpath("/html/body/section/div[1]/aside[2]/div[2]/span[4]/b").get()
            item['manufacterer'] = soup(manufacterer, "lxml").text
        except:
            pass

        try:
            manufacterer_location = response.xpath("/html/body/section/div[1]/aside[2]/div[2]/span[5]/b").get()
            item['manufacterer_location'] = soup(manufacterer_location, "lxml").text
        except:
            pass

        try:
            effect = response.xpath("/html/body/section/div[2]/aside/article[1]/div[2]/p").get()
            item['effect'] = soup(effect, "lxml").text
        except:
            pass

        try:
            side_effect = response.xpath("/html/body/section/div[2]/aside/article[5]/div[2]/p").get()
            item['side_effect'] = soup(side_effect, "lxml").text
        except:
            pass

        try:
            contraindication = response.xpath("/html/body/section/div[2]/aside/article[3]/div[2]/p").get()
            item['contraindication'] = soup(contraindication, "lxml").text
        except:
            pass

        try:
            dosage = response.xpath("/html/body/section/div[2]/aside/article[2]/div[2]").get()
            item['dosage'] = soup(dosage, "lxml").text
        except:
            pass

        try:
            price = response.xpath("/html/body/section/div[1]/aside[2]/div[1]").get()
            item['price'] = soup(price, "lxml").text
        except:
            pass

        item['drugstore_name'] = "Nhà thuốc An Khang"

        logging.info(json.dumps(item))
        yield item

