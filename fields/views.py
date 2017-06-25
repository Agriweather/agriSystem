from django.shortcuts import render
from django.db import connection

from django.http import JsonResponse, HttpResponse
from django.core import serializers
from django.core.files.storage import default_storage
from django.db.models import Q, Count, Avg
from functools import reduce
from .models import FieldLog
import json

"""
from sentence_ponds.models import Sentence
from dictionaries.models import Dictionary
from pondlets.models import DialogueSentence, Pondlet
"""

def postFieldData(request, data):
    # do something
    data_parts = data.split('|')
    parts_count = len(data_parts)

    if parts_count == 2:
      flog = FieldLog.objects.create(sensor=data_parts[0], payload=data_parts[1])
      flog.save();
      flag = "ok"
    else:
      flag = "format error"

    response_data = {}
    response_data['status'] = flag

    return JsonResponse(response_data, safe=False)

