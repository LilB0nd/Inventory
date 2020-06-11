from django.http import HttpResponseRedirect
from django.views import generic
from django.shortcuts import render, get_object_or_404
from .forms import RoomForm, BeamerForm, ComputerForm, ScreenForm, SmartBoardForm, \
    CanvasForm, SpeakerSetForm, RoomUpdateForm
from .models import Room


class IndexView(generic.ListView):
    template_name = 'inventory_managementsentials/index.html'
    context_object_name = "room_list"

    def get_queryset(self):
        return Room.objects.order_by('description')


class RoomDetailView(generic.DetailView):
    model = Room
    template_name = 'inventory_managementsentials/room_detail.html'


def room_create_view(request):
    form = RoomForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = RoomForm
    context = {'form': form}
    return render(request, 'inventory_managementsentials/add_room.html', context)


def beamer_create_view(request):
    form = BeamerForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = BeamerForm
    context = {'form': form}
    return render(request, 'inventory_managementsentials/add_beamer.html', context)


def computer_create_view(request):
    form = ComputerForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ComputerForm
    context = {'form': form}
    return render(request, 'inventory_managementsentials/add_computer.html', context)


def screen_create_view(request):
    form = ScreenForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ScreenForm
    context = {'form': form}
    return render(request, 'inventory_managementsentials/add_screen.html', context)


def smartboard_create_view(request):
    form = SmartBoardForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = SmartBoardForm
    context = {'form': form}
    return render(request, 'inventory_managementsentials/add_smartboard.html', context)


def canvas_create_view(request):
    form = CanvasForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = CanvasForm
    context = {'form': form}
    return render(request, 'inventory_managementsentials/add_canvas.html', context)


def speakerset_create_view(request):
    form = SpeakerSetForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = SpeakerSetForm
    context = {'form': form}
    return render(request, 'inventory_managementsentials/add_speakerset.html', context)


def room_update_view(request, pk):
    instance = get_object_or_404(Room, description=pk)
    form = RoomUpdateForm(request.POST or None, instance=instance)
    if form.is_valid():
        form.save()
    context = {'form': form}
    return render(request, 'inventory_managementsentials/update_room.html', context)



