
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.
# Ruta: /hola
def holaEndpoint(request):
    # Logica de respuesta ante HTTP request
    return HttpResponse("HOLA!!!") 

# Ruta: /adios
def endpoint2(request):
    return HttpResponse("ADIOS!!!") 

# Ruta: /html
def htmlEndpoint(request):
    return HttpResponse("""
        <html>
            <body>
                <h1>Programacion Web</h1>
                <img src="https://upload.wikimedia.org/wikipedia/commons/a/a0/Universidad_de_Lima_logo.png" />
                <form method="post" action="/prueba/post">
                    <input type="text" name="username" />
                    <input type="password" name="password" />
                    <button type="submit">Enviar</button>
                </form>
            </body>
        </html>
    """)

# Ruta: /post
@csrf_exempt
def postFormularioEndpoint(request):
    if request.method == "POST":
        usuario = request.POST.get("username")
        password = request.POST.get("password")
        return HttpResponse(f"""
            <p>Usuario: {usuario}</p>
            <p>Password: {password}</p>
        """)

    return HttpResponse("Llego")

def getQueryParameters(request):
    if request.method == "GET":
        usuario = request.GET.get("usu")
        password = request.GET.get("pass")
        return HttpResponse(f"""
            <p>Usuario: {usuario}</p>
            <p>Password: {password}</p>
        """)

def getPathParameters(request, username, password):
    if request.method == "GET":
        return HttpResponse(f"""
            <p>Usuario: {username}</p>
            <p>Password: {password}</p>
        """)

@csrf_exempt
def getRawData(request):
    if request.method == "POST":
        strBody = request.body
        dictUsuario = json.loads(strBody) # Convierte string (json)= -> dict python
        jsonUsuario = json.dumps(dictUsuario) # Convierte dict python -> string (json)

        return HttpResponse(jsonUsuario)