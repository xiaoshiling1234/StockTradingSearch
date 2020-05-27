import pymysql
from sqlalchemy import create_engine
import tushare as ts
from scrapy.utils.project import get_project_settings
class get_company_his():
    def __init__(self):
        settings = get_project_settings()
        self.conn = pymysql.connect(
            host=settings['DBHOST'],
            user=settings['DBUSER'],
            port=settings['DBPORT'],
            password=settings['DBPASSWORD'],
            database=settings['DBDATABASE'],
            charset=settings['DBCHARSET'])
        cursor = self.conn.cursor()
        sql = '''
                select distinct code from crawler.longhuthsitem
                '''
        cursor.execute(sql)
        results_db = cursor.fetchall()
        self.codes = []
        for row in results_db:
            self.codes.append(row[0])
        print(self.codes)
        sql ='''
        drop table if exists company_his;
        '''
        cursor.execute(sql)
        self.conn.commit()

    def insert_his(self):
        conn = create_engine('mysql+pymysql://root:123456@localhost:3306/crawler?charset=utf8')
        for code in self.codes:
            # 一次性获取全部日k线数据
            df=ts.get_hist_data(code)
            df['code']=code
            df=df.reset_index()
            df.to_sql('company_his', con=conn, if_exists='append',index=False)

if __name__ == '__main__':
    get_company_his().insert_his()
