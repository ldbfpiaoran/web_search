from django.shortcuts import render
import logging
from django.conf import settings
from scantool.tool.cmscan import *
import scantool.tool.rule
import pymysql
from django.core.paginator import Paginator, InvalidPage, EmptyPage, PageNotAnInteger
from scantool.models import *

logger = logging.getLogger('scantool.views')






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
        search = request.GET.get('search')
        if search :
            search = search.replace(' ','')
            result_list = httpdata.objects.filter(ip__contains=search)
        result_list = getPage(request,result_list)
    except Exception as e:
        print(e)
        logger.error(e)
    return render(request,'search.html',locals())



def getPage(request, result_list):
    paginator = Paginator(result_list, 10)
    try:
        page = int(request.GET.get('page', 1))
        result_list = paginator.page(page)
    except (EmptyPage, InvalidPage, PageNotAnInteger):
        result_list = paginator.page(1)
    return result_list
