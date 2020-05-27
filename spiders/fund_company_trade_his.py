# -*- coding: utf-8 -*-
import pymysql
import scrapy
from scrapy import cmdline
from scrapy.utils.project import get_project_settings

from items import FundCompanyTradeHisItem


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
        select distinct fund_company,fund_company_href from longhutop5thsitem where fund_company not like '%专用%'
        '''
        cursor.execute(sql)
        results_db = cursor.fetchall()
        self.start_urls = []
        for row in results_db:
            self.start_urls.append(row[1])

    def parse(self, response):
        fund_company_name=response.css('.page-row h2::text').extract_first()
        for tr in response.css('.zdph tbody tr'):
            res = tr.css('td')
            item = FundCompanyTradeHisItem()
            item['date']=res[0].css('::text').extract_first()
            item['fund_company_name'] = fund_company_name
            item['stock_name'] = res[1].css('a::text').extract_first()
            item['reason'] = res[2].css('::text').extract_first()
            item['price_change_rate'] = res[3].css('::text').extract_first()
            item['purchases'] = res[4].css('::text').extract_first()
            item['sell'] = res[5].css('::text').extract_first()
            item['net_amount'] = res[6].css('::text').extract_first()
            item['block_name'] = res[7].css('::text').extract_first()
            yield item

        total_num=1
        try:
            total_num=int(response.css('.zdph .page_info::text').extract_first().split('/')[1])
        except Exception as e:
            print(e)

        if total_num>1:
            for page in range(2,total_num+1):
                _url=str(response.request.url).replace('market/lhbyyb','ifmarket/lhbhistory')\
                +"field/ENDDATE/order/desc/page/{}/".format(page)
                yield scrapy.Request(_url, callback=self.parse_next,meta={'fund_company_name': fund_company_name})
        pass

    def parse_next(self,response):
        fund_company_name = response.meta['fund_company_name']
        for tr in response.css('tbody tr'):
            res = tr.css('td')
            item = FundCompanyTradeHisItem()
            item['date'] = res[0].css('::text').extract_first()
            item['fund_company_name'] = fund_company_name
            item['stock_name'] = res[1].css('a::text').extract_first()
            item['reason'] = res[2].css('::text').extract_first()
            item['price_change_rate'] = res[3].css('::text').extract_first()
            item['purchases'] = res[4].css('::text').extract_first()
            item['sell'] = res[5].css('::text').extract_first()
            item['net_amount'] = res[6].css('::text').extract_first()
            item['block_name'] = res[7].css('::text').extract_first()
            yield item
        pass

if __name__ == '__main__':
    cmdline.execute('scrapy crawl fund_company_trade_his -a date=20200525'.split())
