from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("grabar_datos", views.grabar_datos, name="grabar_datos"),
]