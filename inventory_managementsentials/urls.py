from django.conf.urls import url

from . import views
from .views import room_create_view, beamer_create_view, computer_create_view, \
    screen_create_view, smartboard_create_view, canvas_create_view, speakerset_create_view, \
    room_update_view
app_name = "inventory_managementsentials"

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^room/(?P<pk>.+)/$', views.RoomDetailView.as_view(), name='room'),
    url(r'add/room/$', room_create_view),
    url(r'add/beamer/$', beamer_create_view),
    url(r'add/computer/$', computer_create_view),
    url(r'add/screen/$', screen_create_view),
    url(r'add/smartboard/$', smartboard_create_view),
    url(r'add/canvas/$', canvas_create_view),
    url(r'add/speakerset/$', speakerset_create_view),
    url(r'update/room/(?P<pk>.+)/$', room_update_view)
    ]
