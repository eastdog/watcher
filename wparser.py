# -*- coding: utf-8 -*-

__author__ = 'victor'

import json
import crawler

def parse_wcfgb(page, acrawler=None, num_attempt=1):

    """
    parse a html page from weicaifu gold price api
    :param page: html content
    :return:price of goldbar
    """
    try:
       content = json.loads(page)
       return float(content.get('results').get('buy'))
    except Exception, e:
        print 'catch an exception %s time(s)'%num_attempt
        num_attempt += 1
        return parse_wcfgb(page, acrawler, num_attempt) if (num_attempt<3 and acrawler) else False

if __name__ == '__main__':

    crl = crawler.Crawler()

    url_wcfgb = 'http://www.vip9999.com/?s=api-getgold'
    print parse_wcfgb(crl.fetch(url_wcfgb))