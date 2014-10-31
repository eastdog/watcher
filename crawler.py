# -*- coding: utf-8 -*-

__author__ = 'victor'

import urllib2
import spidertools
from useragent import UserAgent

class Crawler():

    def __init__(self, proxy=False, mode='default'):

        self.proxy = spidertools.get_proxy()[0] if proxy else None
        self.mode = mode

    def fetch(self, urlstr):

        if self.mode == 'default':
            request = self.__add_header(urlstr)
            try:
                response = urllib2.urlopen(request)
                return response.read()
            except Exception, e:
                print 'fetch webpage failed', urlstr, e.message
                return


    def __add_header(self, urlstr):

        """
        add headers for a url, return a request
        """
        request = urllib2.Request(urlstr)
        # request.add_header('Referer', "http://www.xiami.com")
        request.add_header("Accept-Language", "zh-cn")
        request.add_header("Accept", 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8')
        request.add_header("Connection", "keep-alive")
        agent = UserAgent.get_browser()
        request.add_header(agent[0], agent[1])
        if self.proxy:
            request.set_proxy(self.proxy, 'http')
        return request
