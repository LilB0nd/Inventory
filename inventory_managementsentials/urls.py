from django.conf.urls import url

from . import views
from .views import *
app_name = "inventory_managementsentials"

urlpatterns = [
    url('^$',views.Home.as_view(),name='home'),
    url(r'^room/all/$', views.RoomView.as_view(), name='RoomView'),
    url(r'^room/(?P<pk>.+)/$', views.RoomDetailView.as_view(), name='room'),
    url(r'^add/room/$', room_create_view,  name='AddRoom'),
    url(r'^delete/room/(?P<pk>.+)/$', room_delete_view, name='DeleteRoom'),
    url(r'^update/room/(?P<pk>.+)/$', room_update_view, name='UpdateRoom'),

    url(r'^device/all$', views.DeviceView.as_view(), name='DeviceView'),

    url(r'^beamer/all$', views.BeamerView.as_view(), name='BeamerView'),
    url(r'^add/beamer/$', beamer_create_view, name='AddBeamer'),
    url(r'^update/beamer/(?P<pk>.+)/$', beamer_update_view, name='UpdateBeamer'),
    url(r'^delete/beamer/(?P<pk>.+)/$', beamer_delete_view, name='DeleteBeamer'),

    url(r'^computer/all$', views.ComputerView.as_view(), name='ComputerView'),
    url(r'^add/computer/$', computer_create_view, name='AddComputer'),
    url(r'^update/computer/(?P<pk>.+)/$', computer_update_view, name='UpdateBeamer'),
    url(r'^delete/computer/(?P<pk>.+)/$', computer_delete_view, name='DeleteComputer'),

    url(r'^screen/all$', views.ScreenView.as_view(), name='ScreenView'),
    url(r'^add/screen/$', screen_create_view, name='AddScreen'),
    url(r'^update/screen/(?P<pk>.+)/$', screen_update_view, name='UpdateScreen'),
    url(r'^delete/screen/(?P<pk>.+)/$', screen_delete_view, name='DeleteScreen'),

    url(r'^smartboard/all$', views.SmartBoardView.as_view(), name='SmartBoardView'),
    url(r'^add/smartboard/$', smartboard_create_view, name='AddSmardboard'),
    url(r'^update/smartboard/(?P<pk>.+)/$', smartboard_update_view, name='UpdateSmartBoard'),
    url(r'^delete/smartboard/(?P<pk>.+)/$', smartboard_delete_view, name='DeleteSmartBoard'),

    url(r'^canvas/all$', views.CanvasView.as_view(), name='CanvasView'),
    url(r'^add/canvas/$', canvas_create_view, name='AddCanvas'),
    url(r'^update/canvas/(?P<pk>.+)/$', canvas_update_view, name='UpdateCanvas'),
    url(r'^delete/canvas/(?P<pk>.+)/$', canvas_delete_view, name='DeleteCanvas'),

    url(r'^speakerset/all$', views.SpeakerSetView.as_view(), name='SpeakerSetView'),
    url(r'^add/speakerset/$', speakerset_create_view, name='AddSpeakerset'),
    url(r'^update/speakerset/(?P<pk>.+)/$', speakerset_update_view, name='UpdateSpeakerSet'),
    url(r'^delete/speakerset/(?P<pk>.+)/$', speakerset_delete_view, name='DeleteSpeakerSet'),

    url(r'^register', views.register, name='register'),
    url(r'^login', views.loginPage, name='login'),
    url(r'^logout', views.logoutUser, name='logout')
    ]
