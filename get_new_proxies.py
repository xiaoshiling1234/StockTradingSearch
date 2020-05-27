# 获取免费的代理并验证代理的可用性
# 爬虫第二部， 找到了xicidaili
import requests
from lxml import etree

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
}


def get_free_proxy():
    url = 'https://www.xicidaili.com/nn/'
    # 爬虫第三步
    response = requests.get(url, headers=headers)
    # with open('xicidaili.html', 'wb') as f:
    #     f.write(response.content)
    html_ele = etree.HTML(response.content)
    tr_eles = html_ele.xpath('//table[@id="ip_list"]//tr')
    tr_eles.pop(0)
    for tr_ele in tr_eles:
        ip_str = tr_ele.xpath('./td[2]/text()')[0]
        port = tr_ele.xpath('./td[3]/text()')[0]
        yield 'http://' + ip_str + ':' + port


def validate_proxy(proxy_str):
    url = 'http://data.10jqka.com.cn'
    proxy = {
        'http': proxy_str,
        'https': proxy_str
    }
    try:
        response = requests.get(url, proxies=proxy, timeout=5)
        if response.status_code == 200:
            print('这个代理好使！！！', proxy_str)
            return True
        else:
            print('这个代理好使！！！', proxy_str)
            return True
    except:
        print('什么玩意， 不好使', proxy_str)
        return False


if __name__ == '__main__':
    fp=open('ip.txt','w+',encoding='utf-8')
    good_proxy = []
    for item in get_free_proxy():
        if validate_proxy(item):
            fp.writelines(item+"\n")