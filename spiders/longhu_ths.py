# -*- coding: utf-8 -*-
import scrapy
from scrapy import cmdline
from items import LonghuTHSItem,LonghuTop5THSItem

class LonghuThsSpider(scrapy.Spider):
    name = 'longhu_ths'
    allowed_domains = ['data.10jqka.com.cn']

    def __init__(self, date=None, *args, **kwargs):
        super(LonghuThsSpider, self).__init__(*args, **kwargs)
        self.start_urls = ['http://data.10jqka.com.cn/ifmarket/lhbggxq/report/%s/' % date]

#     start_urls = ['http://data.10jqka.com.cn/ifmarket/lhbggxq/report/2020-05-06/'
# ,'http://data.10jqka.com.cn/ifmarket/lhbggxq/report/2020-05-07/'
# ,'http://data.10jqka.com.cn/ifmarket/lhbggxq/report/2020-05-08/'
# ,'http://data.10jqka.com.cn/ifmarket/lhbggxq/report/2020-05-09/'
# ,'http://data.10jqka.com.cn/ifmarket/lhbggxq/report/2020-05-10/'
# ,'http://data.10jqka.com.cn/ifmarket/lhbggxq/report/2020-05-11/'
# ,'http://data.10jqka.com.cn/ifmarket/lhbggxq/report/2020-05-12/'
# ,'http://data.10jqka.com.cn/ifmarket/lhbggxq/report/2020-05-13/'
# ,'http://data.10jqka.com.cn/ifmarket/lhbggxq/report/2020-05-14/'
# ,'http://data.10jqka.com.cn/ifmarket/lhbggxq/report/2020-05-15/'
# ,'http://data.10jqka.com.cn/ifmarket/lhbggxq/report/2020-05-16/'
# ,'http://data.10jqka.com.cn/ifmarket/lhbggxq/report/2020-05-17/'
# ,'http://data.10jqka.com.cn/ifmarket/lhbggxq/report/2020-05-18/'
# ,'http://data.10jqka.com.cn/ifmarket/lhbggxq/report/2020-05-19/'
# ,'http://data.10jqka.com.cn/ifmarket/lhbggxq/report/2020-05-20/'
# ,'http://data.10jqka.com.cn/ifmarket/lhbggxq/report/2020-05-21/'
# ,'http://data.10jqka.com.cn/ifmarket/lhbggxq/report/2020-05-22/'
# ,'http://data.10jqka.com.cn/ifmarket/lhbggxq/report/2020-05-23/'
# ,'http://data.10jqka.com.cn/ifmarket/lhbggxq/report/2020-05-24/'
# ,'http://data.10jqka.com.cn/ifmarket/lhbggxq/report/2020-05-25/']

    def parse(self, response):
        date=response.request.url.split('/')[-2]
        # response_body=response.body.decode(response.encoding)
        # print(response_body)
        for item in response.css('.twrap tr'):
            ths_item = LonghuTHSItem()
            info = item.css('td')
            ths_item['code']=info[1].css('::text').extract_first()
            ths_item['name'] = info[2].css('a::text').extract_first()
            ths_item['href'] = info[2].css('a::attr(href)').extract_first()
            ths_item['price'] = info[3].css('::text').extract_first()
            ths_item['price_change_rate'] = info[4].css('::text').extract_first()
            ths_item['trading_volume'] = info[5].css('::text').extract_first()
            ths_item['purchases'] = info[6].css('::text').extract_first()
            ths_item['date'] = date
            yield ths_item

        for item in response.css('.stockcont'):
            m_table=item.css('.m-table')
            for company in m_table[0].css('tbody tr'):
                top_ths_item = LonghuTop5THSItem()
                top_ths_item['code']=item.css('::attr(stockcode)').extract_first()
                top_ths_item['title'] = '买入金额最大的前5名营业部'
                tds = company.css('td')
                top_ths_item['fund_company'] = tds[0].css('a::text').extract_first()
                top_ths_item['fund_company_href'] = tds[0].css('a::attr(href)').extract_first()
                top_ths_item['purchases'] = tds[1].css('::text').extract_first()
                top_ths_item['sell'] = tds[2].css('::text').extract_first()
                top_ths_item['net_amount'] = tds[3].css('::text').extract_first()
                top_ths_item['date'] = date
                yield top_ths_item

            for company in m_table[1].css('tbody tr'):
                top_ths_item = LonghuTop5THSItem()
                top_ths_item['code']=item.css('::attr(stockcode)').extract_first()
                top_ths_item['title'] = '卖出金额最大的前5名营业部'
                tds = company.css('td')
                top_ths_item['fund_company'] = tds[0].css('a::text').extract_first()
                top_ths_item['fund_company_href'] = tds[0].css('a::attr(href)').extract_first()
                top_ths_item['purchases'] = tds[1].css('::text').extract_first()
                top_ths_item['sell'] = tds[2].css('::text').extract_first()
                top_ths_item['net_amount'] = tds[3].css('::text').extract_first()
                top_ths_item['date'] = date
                yield top_ths_item
        pass

if __name__ == '__main__':
    cmdline.execute('scrapy crawl longhu_ths -a date=20200525'.split())