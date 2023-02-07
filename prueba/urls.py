from django.urls import path

from . import views

urlpatterns = [
    path("hola", views.holaEndpoint),
    path("adios", views.endpoint2),
    path("html", views.htmlEndpoint),
    path("post", views.postFormularioEndpoint),
    path("get-query", views.getQueryParameters),
    path("get-path/<str:username>/<str:password>", views.getPathParameters),
    path("post-raw", views.getRawData)
]