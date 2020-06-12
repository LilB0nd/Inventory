from django.views import generic
from django.shortcuts import render, get_object_or_404, redirect
from .forms import RoomForm, BeamerForm, ComputerForm, ScreenForm, SmartBoardForm, \
    CanvasForm, SpeakerSetForm, CreateUserForm
from .models import Room, Beamer, Computer, Screen, SmartBoard, Canvas, SpeakerSet
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

class Home(generic.ListView,):
    template_name = 'inventory_managementsentials/links.html'
    def get_queryset(self):
        return None

class RoomView(LoginRequiredMixin, generic.ListView):
    login_url = 'inventory_managementsentials:login'
    template_name = 'inventory_managementsentials/all/all_rooms.html'
    context_object_name = "room_list"

    def get_queryset(self):
        filter_description = self.request.GET.get('room_description', None)
        if filter_description is not None:
            return Room.objects.filter(description__icontains=filter_description)
        else:
            return Room.objects.order_by('description')


class BeamerView(LoginRequiredMixin, generic.ListView):
    login_url = 'inventory_managementsentials:login'
    template_name = 'inventory_managementsentials/all/all_beamers.html'
    context_object_name = 'beamer_list'

    def get_queryset(self):
        filter_description = self.request.GET.get('beamer_description', None)
        if filter_description is not None:
            print(Beamer.objects.filter(description__icontains=filter_description))
            return Beamer.objects.filter(description__icontains=filter_description)
        else:
            return Beamer.objects.order_by('description')


class RoomDetailView(LoginRequiredMixin, generic.DetailView):
    login_url = 'inventory_managementsentials:login'
    template_name = 'inventory_managementsentials/room_detail.html'
    model = Room


class DeviceView(LoginRequiredMixin, generic.ListView):
    login_url = 'inventory_managementsentials:login'
    template_name = 'inventory_managementsentials/all/all_device.html'

    def get_queryset(self):
        return None

    def get_context_data(self, *, object_list=None, **kwargs, ):
        context = super().get_context_data(**kwargs)
        context['beamer_list'] = Beamer.objects.order_by('description')
        context['computer_list'] = Computer.objects.order_by('description')
        context['screen_list'] = Screen.objects.order_by('description')
        context['smartboard_list'] = SmartBoard.objects.order_by('description')
        context['canvas_list'] = Canvas.objects.order_by('description')
        context['speakerset_list'] = SpeakerSet.objects.order_by('description')

        filter_description = self.request.GET.get('description', None)
        if filter_description is not None:
            context['beamer_list'] = Beamer.objects.filter(description__icontains=filter_description)
            context['computer_list'] = Computer.objects.filter(description__icontains=filter_description)
            context['screen_list'] = Screen.objects.filter(description__icontains=filter_description)
            context['smartboard_list'] = SmartBoard.objects.filter(description__icontains=filter_description)
            context['canvas_list'] = Canvas.objects.filter(description__icontains=filter_description)
            context['speakerset_list'] = SpeakerSet.objects.filter(description__icontains=filter_description)
            return context

        use = self.request.GET.get("use", None)
        if use is not None:
            context['beamer_list'] = Beamer.objects.exclude(room=None)
            context['computer_list'] = Computer.objects.exclude(room=None)
            context['screen_list'] = Screen.objects.exclude(room=None)
            context['smartboard_list'] = SmartBoard.objects.exclude(room=None)
            context['canvas_list'] = Canvas.objects.exclude(room=None)
            context['speakerset_list'] = SpeakerSet.objects.exclude(room=None)

        return context


class ComputerView(LoginRequiredMixin, generic.ListView):
    login_url = 'inventory_managementsentials:login'
    template_name = 'inventory_managementsentials/all/all_computer.html'
    context_object_name = 'computer_list'

    def get_queryset(self):
        filter_description = self.request.GET.get('computer_description', None)
        if filter_description is not None:
            return Computer.objects.filter(description__icontains=filter_description)
        else:
            return Computer.objects.order_by('description')


class ScreenView(LoginRequiredMixin, generic.ListView):
    login_url = 'inventory_managementsentials:login'
    template_name = 'inventory_managementsentials/all/all_screens.html'
    context_object_name = 'screen_list'

    def get_queryset(self):
        filter_description = self.request.GET.get('screen_description', None)
        if filter_description is not None:
            return Screen.objects.filter(description__icontains=filter_description)
        else:
            return Screen.objects.order_by('description')


class SmartBoardView(LoginRequiredMixin, generic.ListView):
    login_url = 'inventory_managementsentials:login'
    template_name = 'inventory_managementsentials/all/all_smartboard.html'
    context_object_name = 'smartboard_list'

    def get_queryset(self):
        filter_description = self.request.GET.get('smartboard_description', None)
        if filter_description is not None:
            return SmartBoard.objects.filter(description__icontains=filter_description)
        else:
            return SmartBoard.objects.order_by('description')


class CanvasView(LoginRequiredMixin, generic.ListView):
    login_url = 'inventory_managementsentials:login'
    template_name = 'inventory_managementsentials/all/all_canvas.html'
    context_object_name = 'canvas_list'

    def get_queryset(self):
        filter_description = self.request.GET.get('canvas_description', None)
        if filter_description is not None:
            return Canvas.objects.filter(description__icontains=filter_description)
        else:
            return Canvas.objects.order_by('description')


class SpeakerSetView(LoginRequiredMixin, generic.ListView):
    login_url = 'inventory_managementsentials:login'
    template_name = 'inventory_managementsentials/all/all_speakerset.html'
    context_object_name = 'speakerset_list'

    def get_queryset(self):
        filter_description = self.request.GET.get('speakerset_description', None)
        if filter_description is not None:
            return SpeakerSet.objects.filter(description__icontains=filter_description)
        else:
            return SpeakerSet.objects.order_by('description')


@login_required(login_url='inventory_managementsentials:login')
def room_create_view(request):
    form = RoomForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('inventory_managementsentials:RoomView')

    context = {'form': form}
    return render(request, 'inventory_managementsentials/add/add_room.html', context)


@login_required(login_url='inventory_managementsentials:login')
def room_delete_view(request, pk):
    get_object_or_404(Room, description=pk).delete()
    return redirect('inventory_managementsentials:RoomView')


@login_required(login_url='inventory_managementsentials:login')
def room_update_view(request, pk):
    instance = get_object_or_404(Room, description=pk)
    form = RoomForm(request.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        return redirect('inventory_managementsentials:room', pk)

    context = {'form': form}
    return render(request, 'inventory_managementsentials/update/update_room.html', context)


@login_required(login_url='inventory_managementsentials:login')
def beamer_create_view(request):
    form = BeamerForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('inventory_managementsentials:BeamerView')

    context = {'form': form}
    return render(request, 'inventory_managementsentials/add/add_beamer.html', context)


@login_required(login_url='inventory_managementsentials:login')
def beamer_delete_view(request, pk):
    get_object_or_404(Beamer, description=pk).delete()
    return redirect('inventory_managementsentials:BeamerView')


@login_required(login_url='inventory_managementsentials:login')
def beamer_update_view(request, pk):
    instance = get_object_or_404(Beamer, description=pk)
    form = BeamerForm(request.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        return redirect('inventory_managementsentials:BeamerView')

    context = {'form': form}
    return render(request, 'inventory_managementsentials/update/update_beamer.html', context)


@login_required(login_url='inventory_managementsentials:login')
def computer_create_view(request):
    form = ComputerForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('inventory_managementsentials:ComputerView')

    context = {'form': form}
    return render(request, 'inventory_managementsentials/add/add_computer.html', context)


@login_required(login_url='inventory_managementsentials:login')
def computer_delete_view(request, pk):
    get_object_or_404(Computer, description=pk).delete()
    return redirect('inventory_managementsentials:ComputerView')


@login_required(login_url='inventory_managementsentials:login')
def computer_update_view(request, pk):
    instance = get_object_or_404(Computer, description=pk)
    form = ComputerForm(request.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        return redirect('inventory_managementsentials:ComputerView')

    context = {'form': form}
    return render(request, 'inventory_managementsentials/update/update_computer.html', context)


@login_required(login_url='inventory_managementsentials:login')
def screen_create_view(request):
    form = ScreenForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('inventory_managementsentials:ScreenView')

    context = {'form': form}
    return render(request, 'inventory_managementsentials/add/add_screen.html', context)


@login_required(login_url='inventory_managementsentials:login')
def screen_delete_view(request, pk):
    get_object_or_404(Screen, description=pk).delete()
    return redirect('inventory_managementsentials:ScreenView')


@login_required(login_url='inventory_managementsentials:login')
def screen_update_view(request, pk):
    instance = get_object_or_404(Screen, description=pk)
    form = ScreenForm(request.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        return redirect('inventory_managementsentials:ScreenView')

    context = {'form': form}
    return render(request, 'inventory_managementsentials/update/update_screen.html', context)


@login_required(login_url='inventory_managementsentials:login')
def smartboard_create_view(request):
    form = SmartBoardForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('inventory_managementsentials:SmartBoardView')

    context = {'form': form}
    return render(request, 'inventory_managementsentials/add/add_smartboard.html', context)


@login_required(login_url='inventory_managementsentials:login')
def smartboard_delete_view(request, pk):
    get_object_or_404(SmartBoard, description=pk).delete()
    return redirect('inventory_managementsentials:SmartBoardView')


@login_required(login_url='inventory_managementsentials:login')
def smartboard_update_view(request, pk):
    instance = get_object_or_404(SmartBoard, description=pk)
    form = SmartBoardForm(request.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        return redirect('inventory_managementsentials:SmartBoardView')

    context = {'form': form}
    return render(request, 'inventory_managementsentials/update/update_smartboard.html', context)


@login_required(login_url='inventory_managementsentials:login')
def canvas_create_view(request):
    form = CanvasForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('inventory_managementsentials:CanvasView')

    context = {'form': form}
    return render(request, 'inventory_managementsentials/add/add_canvas.html', context)


@login_required(login_url='inventory_managementsentials:login')
def canvas_delete_view(request, pk):
    get_object_or_404(Canvas, description=pk).delete()
    return redirect('inventory_managementsentials:CanvasView')


@login_required(login_url='inventory_managementsentials:login')
def canvas_update_view(request, pk):
    instance = get_object_or_404(Canvas, description=pk)
    form = CanvasForm(request.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        return redirect('inventory_managementsentials:CanvasView')

    context = {'form': form}
    return render(request, 'inventory_managementsentials/update/update_canvas.html', context)


@login_required(login_url='inventory_managementsentials:login')
def speakerset_create_view(request):
    form = SpeakerSetForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('inventory_managementsentials:SpeakerSetView')

    context = {'form': form}
    return render(request, 'inventory_managementsentials/add/add_speakerset.html', context)


@login_required(login_url='inventory_managementsentials:login')
def speakerset_delete_view(request, pk):
    get_object_or_404(SpeakerSet, description=pk).delete()
    return redirect('inventory_managementsentials:SpeakerSetView')


@login_required(login_url='inventory_managementsentials:login')
def speakerset_update_view(request, pk):
    instance = get_object_or_404(SpeakerSet, description=pk)
    form = SpeakerSetForm(request.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        return redirect('inventory_managementsentials:SpeakerSetView')

    context = {'form': form}
    return render(request, 'inventory_managementsentials/update/update_canvas.html', context)


def register(request, ):
    if request.user.is_authenticated:
        return redirect('inventory_managementsentials:RoomView')
    else:
        register_form = CreateUserForm()
        if request.method == "POST":
            register_form = CreateUserForm(request.POST)
            if register_form.is_valid():
                register_form.save()
                return redirect('inventory_managementsentials:login')

        return render(request, 'inventory_managementsentials/register.html', {'register_form': register_form})


def loginPage(request, ):
    if request.user.is_authenticated:
        return redirect('inventory_managementsentials:RoomView')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('inventory_managementsentials:RoomView')
            else:
                messages.info(request, 'Benutzername oder Passwort ist Falsch')

        return render(request, 'inventory_managementsentials/login.html', {'login': login})


def logoutUser(request, ):
    logout(request)
    return redirect('inventory_managementsentials:login')
