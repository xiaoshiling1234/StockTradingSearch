# -*- coding: utf-8 -*-
import pymysql
import scrapy
from scrapy import cmdline

import settings
from items import LonghuTHSItem, LonghuTop5THSItem
from scrapy.utils.project import get_project_settings


class fund_company_trade_his(scrapy.Spider):
    name = 'fund_company_trade_his'
    allowed_domains = ['data.10jqka.com.cn']

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        settings = get_project_settings()
        conn = pymysql.connect(
            host=settings['DBHOST'],
            user=settings['DBUSER'],
            port=settings['DBPORT'],
            password=settings['DBPASSWORD'],
            database=settings['DBDATABASE'],
            charset=settings['DBCHARSET'])
        cursor = conn.cursor()
        sql = '''
        select distinct fund_company,fund_company_href from longhutop5thsitem
        '''
        cursor.execute(sql)
        results_db = cursor.fetchall()
        self.start_urls = []
        for row in results_db:
            self.start_urls.append(row[1])
        print(self.start_urls)

    def parse(self, response):
        pass


if __name__ == '__main__':
    cmdline.execute('scrapy crawl fund_company_trade_his -a date=20200525'.split())
