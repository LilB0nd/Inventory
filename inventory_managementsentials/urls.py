from django.conf.urls import url

from . import views
from .views import room_create_view, beamer_create_view, computer_create_view, \
    screen_create_view, smartboard_create_view, canvas_create_view, speakerset_create_view, \
    room_update_view, beamer_update_view, computer_update_view, screen_update_view, \
    smartboard_update_view, canvas_update_view, speakerset_update_view
app_name = "inventory_managementsentials"

urlpatterns = [
    url(r'^room/all/$', views.RoomView.as_view(), name='RoomView'),
    url(r'^device/all$', views.DeviceView.as_view(), name='DeviceView'),
    url(r'^beamer/all$', views.BeamerView.as_view(), name='BeamerView'),
    url(r'^computer/all$', views.ComputerView.as_view(), name='ComputerView'),
    url(r'^screen/all$', views.ScreenView.as_view(), name='ScreenView'),
    url(r'^smartboard/all$', views.SmartBoardView.as_view(), name='SmartBoardView'),
    url(r'^canvas/all$', views.CanvasView.as_view(), name='CanvasView'),
    url(r'^speakerset/all$', views.SpeakerSetView.as_view(), name='SpeakerSetView'),
    url(r'^room/(?P<pk>.+)/$', views.RoomDetailView.as_view(), name='room'),
    url(r'^add/room/$', room_create_view),
    url(r'^add/beamer/$', beamer_create_view),
    url(r'^add/computer/$', computer_create_view),
    url(r'^add/screen/$', screen_create_view),
    url(r'^add/smartboard/$', smartboard_create_view),
    url(r'^add/canvas/$', canvas_create_view),
    url(r'^add/speakerset/$', speakerset_create_view),
    url(r'^update/room/(?P<pk>.+)/$', room_update_view),
    url(r'^update/beamer/(?P<pk>.+)/$', beamer_update_view),
    url(r'^update/computer/(?P<pk>.+)/$', computer_update_view),
    url(r'^update/screen/(?P<pk>.+)/$', screen_update_view),
    url(r'^update/smartboard/(?P<pk>.+)/$', smartboard_update_view),
    url(r'^update/canvas/(?P<pk>.+)/$', canvas_update_view),
    url(r'^update/speakerset/(?P<pk>.+)/$', speakerset_update_view),
    url(r'^register',views.register,name='register'),
    url(r'^login', views.loginPage, name='login'),
    url(r'^logout', views.logoutUser, name='logout')
    ]
#url(r'^$', views.IndexView.as_view(), name='index'),