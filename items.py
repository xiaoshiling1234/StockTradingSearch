# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class GupiaoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class LonghuTHSItem(scrapy.Item):
    code = scrapy.Field()
    name = scrapy.Field()
    href = scrapy.Field()
    price = scrapy.Field()
    price_change_rate = scrapy.Field()
    trading_volume = scrapy.Field()
    purchases = scrapy.Field()
    date = scrapy.Field()

class LonghuTop5THSItem(scrapy.Item):
    code = scrapy.Field()
    title = scrapy.Field()
    fund_company = scrapy.Field()
    fund_company_href = scrapy.Field()
    purchases = scrapy.Field()
    sell = scrapy.Field()
    net_amount = scrapy.Field()
    date = scrapy.Field()

class FundCompanyTradeHisItem(scrapy.Item):
    date = scrapy.Field()
    fund_company_name = scrapy.Field()
    stock_name = scrapy.Field()
    reason = scrapy.Field()
    price_change_rate = scrapy.Field()
    purchases = scrapy.Field()
    sell = scrapy.Field()
    net_amount = scrapy.Field()
    block_name = scrapy.Field()
