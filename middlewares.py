# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html
import random
from scrapy.utils.project import get_project_settings
from scrapy import signals


class GupiaoSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class GupiaoDownloaderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


# Scrapy 内置的 Downloader Middleware 为 Scrapy 供了基础的功能，
# 定义一个类，其中（object）可以不写，效果一样
class SimpleProxyMiddleware(object):
    settings = get_project_settings()
    # 声明一个数组
    proxyList = settings['PROXYLIST']

    # Downloader Middleware的核心方法，只有实现了其中一个或多个方法才算自定义了一个Downloader Middleware
    def process_request(self, request, spider):
        # 随机从其中选择一个，并去除左右两边空格
        proxy = random.choice(self.proxyList).strip()
        # 打印结果出来观察
        print("this is request ip:" + proxy)
        # 设置request的proxy属性的内容为代理ip
        request.meta['proxy'] = proxy

    # Downloader Middleware的核心方法，只有实现了其中一个或多个方法才算自定义了一个Downloader Middleware
    def process_response(self, request, response, spider):
        # 请求失败不等于200
        if response.status != 200:
            # 重新选择一个代理ip
            proxy = random.choice(self.proxyList).strip()
            print("this is response ip:" + proxy)
            # 设置新的代理ip内容
            request.mete['proxy'] = proxy
            return request
        return response