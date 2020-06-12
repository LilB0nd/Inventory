from django.http import HttpResponseRedirect
from django.views import generic
from django.shortcuts import render, get_object_or_404, redirect
from .forms import RoomForm, BeamerForm, ComputerForm, ScreenForm, SmartBoardForm, \
    CanvasForm, SpeakerSetForm, CreateUserForm
from .models import Room, Beamer, Computer, Screen, SmartBoard, Canvas, SpeakerSet
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout



class RoomView(generic.ListView):
    template_name = 'inventory_managementsentials/all/all_rooms.html'
    context_object_name = "room_list"

    def get_queryset(self):
        filter_description = self.request.GET.get('room_description', None)
        if filter_description is not None:
            return Room.objects.filter(description__icontains=filter_description)
        else:
            return Room.objects.order_by('description')


class BeamerView(generic.ListView):
    template_name = 'inventory_managementsentials/all/all_beamers.html'
    context_object_name = 'beamer_list'

    def get_queryset(self):
        filter_description = self.request.GET.get('beamer_description', None)
        if filter_description is not None:
            print(Beamer.objects.filter(description__icontains=filter_description))
            return Beamer.objects.filter(description__icontains=filter_description)
        else:
            return Beamer.objects.order_by('description')


class ComputerView(generic.ListView):
    template_name = 'inventory_managementsentials/all/all_computer.html'
    context_object_name = 'computer_list'

    def get_queryset(self):
        filter_description = self.request.GET.get('computer_description', None)
        if filter_description is not None:
            return Computer.objects.filter(description__icontains=filter_description)
        else:
            return Computer.objects.order_by('description')


class ScreenView(generic.ListView):
    template_name = 'inventory_managementsentials/all/all_screens.html'
    context_object_name = 'screen_list'

    def get_queryset(self):
        filter_description = self.request.GET.get('screen_description', None)
        if filter_description is not None:
            return Screen.objects.filter(description__icontains=filter_description)
        else:
            return Screen.objects.order_by('description')


class SmartBoardView(generic.ListView):
    template_name = 'inventory_managementsentials/all/all_smartboard.html'
    context_object_name = 'smartboard_list'

    def get_queryset(self):
        filter_description = self.request.GET.get('smartboard_description', None)
        if filter_description is not None:
            return SmartBoard.objects.filter(description__icontains=filter_description)
        else:
            return SmartBoard.objects.order_by('description')


class CanvasView(generic.ListView):
    template_name = 'inventory_managementsentials/all/all_canvas.html'
    context_object_name = 'canvas_list'

    def get_queryset(self):
        filter_description = self.request.GET.get('canvas_description', None)
        if filter_description is not None:
            return Canvas.objects.filter(description__icontains=filter_description)
        else:
            return Canvas.objects.order_by('description')


class SpeakerSetView(generic.ListView):
    template_name = 'inventory_managementsentials/all/all_smartboard.html'
    context_object_name = 'smartboard_list'

    def get_queryset(self):
        filter_description = self.request.GET.get('skeaperset_description', None)
        if filter_description is not None:
            return SpeakerSet.objects.filter(description__icontains=filter_description)
        else:
            return SpeakerSet.objects.order_by('description')


class RoomDetailView(generic.DetailView):
    model = Room
    template_name = 'inventory_managementsentials/room_detail.html'


def room_create_view(request):
    form = RoomForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('inventory_managementsentials:RoomView')

    context = {'form': form}
    return render(request, 'inventory_managementsentials/add/add_room.html', context)


def room_update_view(request, pk):
    instance = get_object_or_404(Room, description=pk)
    form = RoomForm(request.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        return redirect('inventory_managementsentials:RoomView', pk)

    context = {'form': form}
    return render(request, 'inventory_managementsentials/update/update_room.html', context)


def beamer_create_view(request):
    form = BeamerForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('inventory_managementsentials:RoomView')

    context = {'form': form}
    return render(request, 'inventory_managementsentials/add/add_beamer.html', context)


def beamer_update_view(request, pk):
    instance = get_object_or_404(Beamer, description=pk)
    form = BeamerForm(request.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        return redirect('inventory_managementsentials:RoomView')

    context = {'form': form}
    return render(request, 'inventory_managementsentials/update/update_beamer.html', context)


def computer_create_view(request):
    form = ComputerForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('inventory_managementsentials:RoomView')

    context = {'form': form}
    return render(request, 'inventory_managementsentials/add/add_computer.html', context)


def computer_update_view(request, pk):
    instance = get_object_or_404(Computer, description=pk)
    form = ComputerForm(request.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        return redirect('inventory_managementsentials:RoomView')

    context = {'form': form}
    return render(request, 'inventory_managementsentials/update/update_computer.html', context)


def screen_create_view(request):
    form = ScreenForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('inventory_managementsentials:RoomView')

    context = {'form': form}
    return render(request, 'inventory_managementsentials/add/add_screen.html', context)


def screen_update_view(request, pk):
    instance = get_object_or_404(Screen, description=pk)
    form = ScreenForm(request.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        return redirect('inventory_managementsentials:RoomView')

    context = {'form': form}
    return render(request, 'inventory_managementsentials/update/update_screen.html', context)


def smartboard_create_view(request):
    form = SmartBoardForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('inventory_managementsentials:RoomView')

    context = {'form': form}
    return render(request, 'inventory_managementsentials/add/add_smartboard.html', context)


def smartboard_update_view(request, pk):
    instance = get_object_or_404(SmartBoard, description=pk)
    form = SmartBoardForm(request.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        return redirect('inventory_managementsentials:RoomView')

    context = {'form': form}
    return render(request, 'inventory_managementsentials/update/update_smartboard.html', context)


def canvas_create_view(request):
    form = CanvasForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('inventory_managementsentials:RoomView')

    context = {'form': form}
    return render(request, 'inventory_managementsentials/add/add_canvas.html', context)


def canvas_update_view(request, pk):
    instance = get_object_or_404(Canvas, description=pk)
    form = CanvasForm(request.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        return redirect('inventory_managementsentials:RoomView')

    context = {'form': form}
    return render(request, 'inventory_managementsentials/update/update_canvas.html', context)


def speakerset_create_view(request):
    form = SpeakerSetForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('inventory_managementsentials:RoomView')

    context = {'form': form}
    return render(request, 'inventory_managementsentials/add/add_speakerset.html', context)


def speakerset_update_view(request, pk):
    instance = get_object_or_404(SpeakerSet, description=pk)
    form = SpeakerSetForm(request.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        return redirect('inventory_managementsentials:RoomView')

    context = {'form': form}
    return render(request, 'inventory_managementsentials/update/update_canvas.html', context)


def register(request, ):
    register_form = CreateUserForm()
    if request.method == "POST":
        register_form = CreateUserForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            return redirect('inventory_managementsentials:login')

    return render(request, 'inventory_managementsentials/register.html', {'register_form': register_form})


def loginPage(request, ):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('inventory_managementsentials:RoomView')
        else:
            messages.info(request, 'Benutzername oder Passwort ist Falsch')

    return render(request, 'inventory_managementsentials/login.html', {'login':login})


def logoutUser(request, ):
    logout(request)
    return redirect('inventory_managementsentials:login')
