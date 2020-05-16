from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic

from .models import Room


class IndexView(generic.ListView):
    template_name = "inventory_managementsentials/index.html"
    context_object_name = "room_list"

    def get_queryset(self):
        return Room.objects.order_by("description")


def room(request, room_id):
    room_list = Room.objects.all()
    context = {'room_list': room_list[0]}
    return HttpResponse(room_list)
    # output = ", ".join([Room.description for Room in room_list])
    # return render(request, 'inventory_managementsentials/index.html', context)
