# -*- coding: utf-8 -*-
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, HttpResponse
from index.models import News
import requests, json


def index(req):
    context = {}
    context['hello'] = 'Hello MiraclePhone!'
    context['cnt'] = 100
    return render(req, "index.html", context)


def news(req):
    qs = News.objects.all()
    context = {'qs': qs, }
    return render(req, "news.html", context)


def download(req):
    qs = News.objects.all()
    context = {'qs': qs, }
    return render(req, "download.html", context)


def customer(req):
    url = 'http://sh002.miraclephone.cn/api/MiracleNumber/?format=json'
    data = json.dumps({"name": "test_repo", "description": "Some test repo"})
    qs = requests.get(url, data, auth=('admin', 'Kind2021'))
    qs = qs.json()
    str = json.dumps(qs)
    str =str.replace("Number","Numbers")
    qs = json.loads(str)
    context = {}
    context['qs'] = qs
    return render(req, "customer.html", context)


def partner(req):
    qs = News.objects.all()
    context = {'qs': qs, }
    return render(req, "partner.html", context)


def price(req):
    qs = News.objects.all()
    context = {'qs': qs, }
    return render(req, "price.html", context)


def us(req):
    qs = News.objects.all()
    context = {'qs': qs, }
    return render(req, "us.html", context)
