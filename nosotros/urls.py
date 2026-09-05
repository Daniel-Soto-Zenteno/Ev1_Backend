from django.urls import path
from . import views

urlpatterns = [
    path('', views.historia_y_guia, name='historia_y_guia'),
]