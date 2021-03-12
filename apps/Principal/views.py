from django.shortcuts import render

# Create your views here.
def inicio(request):
    email = request.session.get('login')

    context = {

    }

    if not email==None :
        context={
            'email':email
        }

    return render(request, "inicio.html",context)

def cerrarSesion(request):

    del request.session['login']

    context = {
        'context': "Sesión cerrada Correctamente"
    }

    return render(request, "Principal/cerrarSesion.html", context)