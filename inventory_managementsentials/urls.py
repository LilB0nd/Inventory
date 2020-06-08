from django.urls import path

from . import views

app_name = "inventory_managementsentials"

urlpatterns = [
    path("", views.IndexView.as_view(), name='index'),
    ]
