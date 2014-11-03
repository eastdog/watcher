# -*- coding: utf-8 -*-

__author__ = 'victor'

import codecs
import time
import smtplib
from email.mime.text import MIMEText

import crawler
from wparser import parse_wcfgb

def notify(text):

    sender = u'movie_notify@163.com'
    receiver = ['zhouyudong@360iii.com']
    subject = u'Price Update %s日%s时%s分'%(time.localtime()[2:5])
    smtpserver = 'smtp.163.com'
    usr = 'movie_notify'
    pswd = 'sb123456'

    msg = MIMEText(text, _charset='utf-8')
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = ','.join(receiver)

    s = smtplib.SMTP()
    s.connect(smtpserver)
    s.login(usr, pswd)
    s.sendmail(sender, receiver, msg.as_string())
    s.quit()

def record(price):

    print 'current price', price, time.ctime()
    with codecs.open('cach/price', 'a', 'utf-8') as fo:
        fo.write('%s: %s\n'%('.'.join(map(str, time.localtime()[:5])), price))

    return

if __name__ == '__main__':

    crl = crawler.Crawler()
    url_wcfgb = 'http://www.vip9999.com/?s=api-getgold'

    alert = 230

    while True:
        price = parse_wcfgb(crl.fetch(url_wcfgb))
        record(price)
        if price and float(price)<alert:
            notify(price)
        time.sleep(600)