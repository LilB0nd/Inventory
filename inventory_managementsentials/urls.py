from django.conf.urls import url

from . import views

app_name = "inventory_managementsentials"

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'room/(?P<pk>[0-9]+)/$', views.RoomDetailView.as_view(), name='room'),

    ]
