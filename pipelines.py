# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from items import LonghuTop5THSItem, LonghuTHSItem
import json
import pymysql
from scrapy.utils.project import get_project_settings

settings = get_project_settings()


class GupiaoPipeline(object):
    def process_item(self, item, spider):
        return item


class JsonSavePipeline(object):
    def open_spider(self, spider):
        self.LonghuTHSItemFile = open("LonghuTHSItemFile.json", "wb")
        self.LonghuTop5THSItemFile = open("LonghuTop5THSItemFile.json", "wb")

    def process_item(self, item, spider):
        content = json.dumps(dict(item), ensure_ascii=False)
        if isinstance(item, LonghuTHSItem):
            self.LonghuTHSItemFile.write(content.encode("utf-8"))
        elif isinstance(item, LonghuTop5THSItem):
            self.LonghuTop5THSItemFile.write(content.encode("utf-8"))
        return item

    def close_spider(self, spider):
        self.LonghuTHSItemFile.close()
        self.LonghuTop5THSItemFile.close()


class MysqlSavePipeline(object):
    def open_spider(self, spider):
        self.conn = pymysql.connect(
            host=settings['DBHOST'],
            user=settings['DBUSER'],
            port=settings['DBPORT'],
            password=settings['DBPASSWORD'],
            database=settings['DBDATABASE'],
            charset=settings['DBCHARSET'])
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        if isinstance(item, LonghuTHSItem):
            self.saveLonghuTHSItem(item)
        elif isinstance(item, LonghuTop5THSItem):
            self.saveLonghuTop5THSItemFile(item)
        return item

    def saveLonghuTHSItem(self,item):
        assert isinstance(item, LonghuTHSItem)
        sql='''
        insert into LonghuTHSItem(code,name,href,price,price_change_rate,trading_volume,purchases,date) 
        values ('{}','{}','{}','{}','{}','{}','{}','{}')
        '''.format(item['code'],item['name'],item['href'],item['price'],item['price_change_rate'],
        item['trading_volume'],item['purchases'],item['date'])
        self.cursor.execute(sql)
        self.conn.commit()
        # cursor.close()

    def saveLonghuTop5THSItemFile(self,item):
        assert isinstance(item, LonghuTop5THSItem)
        sql='''
        insert into LonghuTop5THSItem(code,title,fund_company,fund_company_href,purchases,sell,net_amount,date) 
        values('{}','{}','{}','{}','{}','{}','{}','{}')
        '''.format(item['code'],item['title'],item['fund_company'],item['fund_company_href'],item['purchases'],
        item['sell'],item['net_amount'],item['date'])
        self.cursor.execute(sql)
        self.conn.commit()
        # cursor.close()

    def close_spider(self, spider):
        self.conn.close()

