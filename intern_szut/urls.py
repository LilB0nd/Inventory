from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path("", views.index, name='index'),
    path('inventory_managementsentials/', include('inventory_managementsentials.urls')),
    path('admin/', admin.site.urls),
]
