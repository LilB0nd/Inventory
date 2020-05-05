from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from .models import Room


def index(request):
    return HttpResponse("In Wartung...")


def room(request, room_id):
    room = Room.objects
    return HttpResponse("You are looking at Room %s" % room_id)
