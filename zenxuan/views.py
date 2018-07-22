# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import JsonResponse
import requests
from rest_framework.decorators import api_view
from top.api import TbkItemGetRequest
import json
import top
import sys
reload(sys)
sys.setdefaultencoding('utf8')

@api_view(['GET','POST'])
def getitem(request,format=None):
    """
     淘宝客商品查询
    """
    if request.method =='GET':
        return JsonResponse({})

    if request.method == 'POST':
        req = TbkItemGetRequest()
        req.set_app_info(top.appinfo(appkey=24646994, secret='7836a9505a7bd2bba94d43169661373a'))
        req_data = json.loads(request.body.decode('utf-8'),encoding='utf-8')
        fields = req_data.get('fields',None)
        q = req_data.get('q',None)
        cat = req_data.get('cat',None)
        itemloc = req_data.get('itemloc',None)
        sort = req_data.get('sort',None)
        is_tmall = req_data.get('is_tamll',None)
        is_overseas = req_data.get('is_overseas',None)
        start_price = req_data.get('start_price',None)
        end_price = req_data.get('end_price',None)
        start_tk_rate = req_data.get('start_tk_rate',None)
        end_tk_rate = req_data.get('end_tk_rate',None)
        platform = req_data.get('platform',None)
        page_no = req_data.get('page_no',None)
        page_size = req_data.get('page_size',None)

        if fields is None:
            req.fields = u"num_iid,title,pict_url,small_images,reserve_price,zk_final_price,user_type,provcity,item_url,seller_id,volume,nick"
        req.q = q if q else u'女装'
        # req.cat = cat if cat else u"16,18"
        if itemloc:
            req.itemloc = itemloc

        req.sort = sort if sort else u"total_sales"
        req.is_tmall = 'true' if is_tmall else 'false'
        req.is_overseas = 'true' if is_overseas else 'false'
        req.start_price = int(start_price) if start_price else 0
        req.end_price = int(end_price) if end_price else 999
        req.start_tk_rate = int(end_tk_rate) if start_tk_rate else 0
        req.end_tk_rate = int(end_tk_rate) if end_tk_rate else 10000
        req.platform = int(platform) if platform else 1
        req.page_no = int(page_no) if page_no else 1
        req.page_size = int(page_size) if page_size else 20
        resp = req.getResponse()
        return JsonResponse(resp)


@api_view(['GET','POST'])
def item_convert(request,format=None):
    """
      淘宝客商品链接转换
    """
    if request.method =='GET':
        return JsonResponse({})

    if request.method == 'POST':
        req = TbkItemGetRequest()
        req.set_app_info(top.appinfo(appkey=24646994, secret='7836a9505a7bd2bba94d43169661373a'))
        req_data = json.loads(request.body.decode('utf-8'),encoding='utf-8')
        fields = req_data.get('fields',None)
        num_iids = req_data.get('num_iids',None)
        adzone_id = req_data.get('adzone_id',None)
        platform = req_data.get('platform',None)
        unid = req_data.get('unid',None)
        dx = req_data.get('dx',None)

        if fields is None:
            req.fields = u"num_iid,click_url"
        if num_iids:
            req.num_iids = num_iids
        if adzone_id:
            req.adzone_id = adzone_id
        if platform:
            req.platform = platform
        if unid:
            req.unid = unid
        if dx:
            req.dx = dx
        resp = req.getResponse()
        return JsonResponse(resp)
