# -*- coding: utf-8 -*-
import scrapy
from sina.items import SinaItem
from scrapy.http import Request

class NewsSinaSpider(scrapy.Spider):
    name = "news_sina"
   # allowed_domains = ["new.sina.com.cn"]
   #start url
    start_urls = (
      'http://news.sina.com.cn/c/nd/2016-09-05/doc-ifxvpxua7896905.shtml?cre=newspagepc&mod=f&loc=1&r=1&doct=0&rfunc=100',
      'http://news.sina.com.cn/c/nd/2016-09-07/doc-ifxvukhx4521882.shtml',
      'http://news.sina.com.cn/w/zx/2016-09-07/doc-ifxvukhx4512372.shtml',
      'http://news.sina.com.cn/w/zx/2016-09-07/doc-ifxvukhx4510865.shtml',
      'http://news.sina.com.cn/o/2016-09-07/doc-ifxvpxua8099408.shtml',
      'http://news.sina.com.cn/o/2016-09-07/doc-ifxvueif6177455.shtml',
      'http://news.sina.com.cn/o/2016-09-03/doc-ifxvpxua7780150.shtml?cre=newspagepc&mod=f&loc=15&r=9&doct=0&rfunc=40',
    )

    def parse(self, response):
        sinaItem=SinaItem()
        links=[]
        sinaItem['url']=response.url
        try:
            sinaItem['docid']=response.xpath('//div/h1[@id="artibodyTitle"]/@docid').extract()[0]
            sinaItem['title']=response.xpath('//div/h1[@id="artibodyTitle"]/text()').extract()[0]
            sinaItem['author']=response.xpath('//p[@class="article-editor"]/text()').extract()[0][5:-1]
            sinaItem['timestamp']=response.xpath('//div/span[@id="navtimeSource"]/text()').extract()[0]
            sinaItem['source']=response.xpath('//div/span[@id="navtimeSource"]//span[@data-sudaclick="media_name"]/a/text()').extract()[0]
            sinaItem['key_words']=response.xpath('//meta[@name="keywords"]/@content').extract()[0]
            pars=response.xpath('//div[@id="artibody"]/p/text()').extract()
            text=''
            for par in pars:
                text+=par
            sinaItem['text']=text
            links=response.xpath('//div[@class="feed-card-item"]/h2/a/@href').extract()
            sinaItem['links']=links
           #just for test
            print sinaItem['title']
            print sinaItem['url']
           # print sinaItem['links']
           # print sinaItem['docid']
           # print sinaItem['author']
           # print sinaItem['timestamp']
           # print sinaItem['source']
           # print sinaItem['key_words']
           # print sinaItem['text']
            yield sinaItem
        except IndexError:
            pass
        for link in links:
            if link.startswith('http://news.sina.com.cn/'):
                yield Request(link,callback=self.parse)
       


