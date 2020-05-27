import scrapy
from scrapy.cmdline import execute

class HttpproxyipSpider(scrapy.Spider):
    # spider 任务名
    name = 'httpProxyIp'
    # 允许访问的域名
    allowed_domains = ['icanhazip.com']
    # 起始爬取的url
    start_urls = ['http://icanhazip.com/']

    # spider 爬虫解析的方法，关于内容的解析都在这里完成; self表示实例的引用， response爬虫的结果
    def parse(self, response):
        print('代理后的ip: ', response.text)

# 这个是main函数也是整个程序入口的惯用写法
if __name__ == '__main__':
    execute(['scrapy', 'crawl', 'httpProxyIp'])