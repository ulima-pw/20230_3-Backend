
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

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
