from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic

from .models import Room, Beamer


class IndexView(generic.ListView):
    template_name = "inventory_managementsentials/index.html"
    context_object_name = "room_list"

    def get_queryset(self):
        return Room.objects.order_by("description")
