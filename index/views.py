# -*- coding: utf-8 -*-
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, HttpResponse
from index.models import News,Service,Park
import requests, json


def index(req):
    context = {}
    context['hello'] = 'Hello MiraclePhone!'
    context['cnt'] = 100
    return render(req, "index.html", context)


def news(req):
    qs = News.objects.all().order_by('updatedtime')
    context = {'qs': qs, }
    return render(req, "news.html", context)


def download(req):
    qs = News.objects.all()
    context = {'qs': qs, }
    return render(req, "download.html", context)

def customer(req):
    url = 'http://www.miracleos.cn/api/users/?format=json'
    data = json.dumps({})
    qs = requests.get(url, data, auth=('admin', 'Kind2021'))
    qs = qs.json()
    str = json.dumps(qs)
    # str =str.replace("127.0.0.1:8001","www.miracleos.cn")
    qs = str
    context = {}
    context['qs'] = qs
    return render(req, "customer.html", context)
def number(req):
    url = 'http://sh002.miraclephone.cn/api/MiracleNumber/?format=json'
    data = json.dumps({"name": "test_repo", "description": "Some test repo"})
    qs = requests.get(url, data, auth=('admin', 'Kind2021'))
    qs = qs.json()
    str = json.dumps(qs)
    str =str.replace("Number","Numbers")
    qs = json.loads(str)
    qs.sort(key= lambda x:x["Stars"],reverse=True)
    context = {}
    context['qs'] = qs
    return render(req, "number.html", context)


def park(req):
    qs = Park.objects.all().order_by('Level')
    context = {'qs': qs, }
    return render(req, "park.html", context)


def price(req):
    qs_P = Service.objects.filter(Type='Phone').order_by('idx')
    qs_B = Service.objects.filter(Type='PBX').order_by('idx')
    qs_N = Service.objects.filter(Type='Number').order_by('idx')
    context = {'qs_P': qs_P,'qs_B':qs_B,'qs_N':qs_N }
    return render(req, "price.html", context)


def us(req):
    qs = News.objects.all()
    context = {'qs': qs, }
    return render(req, "us.html", context)
