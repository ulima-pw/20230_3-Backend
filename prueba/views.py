
from django.http import HttpResponse

# Create your views here.
# Ruta: /hola
def holaEndpoint(request):
    # Logica de respuesta ante HTTP request
    return HttpResponse("HOLA!!!") 

# Ruta: /adios
def endpoint2(request):
    return HttpResponse("ADIOS!!!") 
