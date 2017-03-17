from django.shortcuts import render
import logging
from django.conf import settings
from scantool.tool.cmscan import *
import scantool.tool.rule
import pymysql

logger = logging.getLogger('scantool.views')




def save_data(search):
    try:
        conn = pymysql.connect(host='127.0.0.1', user='root', passwd='521why1314',
                               db='mysql', charset='utf8', port=3306)
        conn = conn.cursor()
        conn.execute('use http_information')
        conn.execute('SELECT * FROM `httpdata` where CONCAT(`ip`,`title`,`header`) like '+'\'%'+search+'%\'')
        result = []
        for i in conn :
            d = {}
            d['url'] = i[1]
            d['title'] = i[2]
            d['header'] = i[3]
            result.append(d)
        return result
    except:
        conn.close()
        return 'none'

def webscan(request):
    try:
        url = request.POST.get('url')
        information = main(url)
    except Exception as e:
        print(e)
        logger.error(e)
    return render(request,'cmscan.html',locals( ))


def search(request):
    try:
        search = request.POST.get('search')
        search = search.replace(' ','')
        result = save_data(search)
    except Exception as e:
        print(e)
        logger.error(e)
    return render(request,'search.html',locals())




