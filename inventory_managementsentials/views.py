from django.http import HttpResponseRedirect
from django.views import generic
from django.shortcuts import render, get_object_or_404, redirect
from .forms import RoomForm, BeamerForm, ComputerForm, ScreenForm, SmartBoardForm, \
    CanvasForm, SpeakerSetForm
from .models import Room, Beamer, Computer, Screen, SmartBoard, Canvas, SpeakerSet
from .filters import RoomFilter

class RoomIndexView(generic.ListView):
    template_name = 'inventory_managementsentials/all_rooms.html'
    context_object_name = "room_list"

    def get_queryset(self):
        return Room.objects.order_by('description')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = RoomFilter(self.request.GET, queryset=self.get_queryset())
        return context

class RoomDetailView(generic.DetailView):
    model = Room
    template_name = 'inventory_managementsentials/room_detail.html'


def room_create_view(request):
    form = RoomForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('inventory_managementsentials:RoomIndexViewr')

    context = {'form': form}
    return render(request, 'inventory_managementsentials/add/add_room.html', context)


def room_update_view(request, pk):
    instance = get_object_or_404(Room, description=pk)
    form = RoomForm(request.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        return redirect('inventory_managementsentials:RoomIndexView', pk)

    context = {'form': form}
    return render(request, 'inventory_managementsentials/update/update_room.html', context)


def beamer_create_view(request):
    form = BeamerForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('inventory_managementsentials:RoomIndexView')

    context = {'form': form}
    return render(request, 'inventory_managementsentials/add/add_beamer.html', context)


def beamer_update_view(request, pk):
    instance = get_object_or_404(Beamer, description=pk)
    form = BeamerForm(request.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        return redirect('inventory_managementsentials:RoomIndexView')

    context = {'form': form}
    return render(request, 'inventory_managementsentials/update/update_beamer.html', context)


def computer_create_view(request):
    form = ComputerForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('inventory_managementsentials:RoomIndexView')

    context = {'form': form}
    return render(request, 'inventory_managementsentials/add/add_computer.html', context)


def computer_update_view(request, pk):
    instance = get_object_or_404(Computer, description=pk)
    form = ComputerForm(request.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        return redirect('inventory_managementsentials:RoomIndexView')

    context = {'form': form}
    return render(request, 'inventory_managementsentials/update/update_computer.html', context)


def screen_create_view(request):
    form = ScreenForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('inventory_managementsentials:RoomIndexView')

    context = {'form': form}
    return render(request, 'inventory_managementsentials/add/add_screen.html', context)


def screen_update_view(request, pk):
    instance = get_object_or_404(Screen, description=pk)
    form = ScreenForm(request.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        return redirect('inventory_managementsentials:RoomIndexView')

    context = {'form': form}
    return render(request, 'inventory_managementsentials/update/update_screen.html', context)


def smartboard_create_view(request):
    form = SmartBoardForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('inventory_managementsentials:RoomIndexView')

    context = {'form': form}
    return render(request, 'inventory_managementsentials/add/add_smartboard.html', context)


def smartboard_update_view(request, pk):
    instance = get_object_or_404(SmartBoard, description=pk)
    form = SmartBoardForm(request.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        return redirect('inventory_managementsentials:RoomIndexView')

    context = {'form': form}
    return render(request, 'inventory_managementsentials/update/update_smartboard.html', context)


def canvas_create_view(request):
    form = CanvasForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('inventory_managementsentials:RoomIndexView')

    context = {'form': form}
    return render(request, 'inventory_managementsentials/add/add_canvas.html', context)


def canvas_update_view(request, pk):
    instance = get_object_or_404(Canvas, description=pk)
    form = CanvasForm(request.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        return redirect('inventory_managementsentials:RoomIndexView')

    context = {'form': form}
    return render(request, 'inventory_managementsentials/update/update_canvas.html', context)


def speakerset_create_view(request):
    form = SpeakerSetForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('inventory_managementsentials:RoomIndexView')

    context = {'form': form}
    return render(request, 'inventory_managementsentials/add/add_speakerset.html', context)


def speakerset_update_view(request, pk):
    instance = get_object_or_404(SpeakerSet, description=pk)
    form = SpeakerSetForm(request.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        return redirect('inventory_managementsentials:RoomIndexView')

    context = {'form': form}
    return render(request, 'inventory_managementsentials/update/update_canvas.html', context)
