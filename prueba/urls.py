from django.urls import path

from . import views

urlpatterns = [
    path("hola", views.holaEndpoint),
    path("adios", views.endpoint2),
    path("html", views.htmlEndpoint),
    path("post", views.postFormularioEndpoint)
]