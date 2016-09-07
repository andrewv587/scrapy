#sina新闻爬虫
  采用分布式架构，实现了抓取新浪新闻的功能。 
  
  将其网站的文章编号，作者，发表时间，关键词，原始网址链接，相关链接，文本等相关信息爬取到mongodb中存储。
##架构：scrapy+redis+mongodb
  其中scrapy_redis文件夹来源于gnemoug/distribute_crawler
##需要依赖的python库：
  redis 
  
  mongodb
##配置：setting.py
###set redis in order to assebly distributed spider
REDIS_HOST = 'docker-ubuntu' 

REDIS_PORT = 16379 

SCHEDULER = "sina.scrapy_redis.scheduler.Scheduler" 

SCHEDULER_PERSIST = False 

SCHEDULER_QUEUE_CLASS = 'sina.scrapy_redis.queue.SpiderPriorityQueue'

###set mongodb to store items
MONGO_URI = "docker-ubuntu" 

MONGO_PORT = 27017 

MONGO_DATABASE = "news_sina" 

MONGO_COLLECTION = "news_items" 

###set logging level 
LOG_LEVEL='INFO' 

初始抓取地址可在sina/spider/start_urls更改

初始为'http://news.sina.com.cn/c/nd/2016-09-05/doc-ifxvpxua7896905.shtml?cre=newspagepc&mod=f&loc=1&r=1&doct=0&rfunc=100'
  
##运行
cd scrapy 

scrapy crawl news_sina&
