from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    html = 'Link zur Adminseite:  <a href=/admin>Adminseite</a>'
    return HttpResponse(html)
