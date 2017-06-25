from django.shortcuts import render
from django.db import connection

from django.http import JsonResponse, HttpResponse
import urllib.parse
from .models import FieldLog
import json


def postFieldData(request, data):
    # do something
    data = urllib.parse.unquote(data)
    data_parts = data.split(',')
    parts_count = len(data_parts)

    """ integrity & security check needed 
        1. check if scheme_id is legitimate
        2. check if user_id is belong the same user
    """
    if parts_count >= 2:
        params = {}
        for i in range(parts_count):
            if i == 0:
                params['field_id']=data_parts[i]
            else:
                stri = str(i)
                stri = stri.zfill(2)
                params['f' + stri]=data_parts[i]
        flog = FieldLog.objects.create(**params)
        flog.save();
        flag = "ok"
    else:
        flag = "format error"

    response_data = {}
    response_data['status'] = flag

    return JsonResponse(response_data, safe=False)

def getFieldData(request):
    # 
    #

    return 1
