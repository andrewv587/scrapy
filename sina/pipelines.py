# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo

class MongoPipeline(object):

    def __init__(self, mongo_uri,mongo_port,mongo_db,mongo_collection):
        self.mongo_uri = mongo_uri
	self.mongo_port = mongo_port
        self.mongo_db = mongo_db
	self.mongo_collection=mongo_collection

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI','localhost'),
	    mongo_port=crawler.settings.get('MONGO_PORT','27017'),
            mongo_db=crawler.settings.get('MONGO_DATABASE', 'news_sina'),
	    mongo_collection=crawler.settings.get('MONGO_COLLECTION', 'news_items')
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri,self.mongo_port)
        self.db = self.client[self.mongo_db]
        self.db[self.mongo_collection].drop()

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        self.db[self.mongo_collection].insert(dict(item))
        return item