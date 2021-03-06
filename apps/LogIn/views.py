from django.shortcuts import render, redirect
from .forms import RegForm
# Create your views here.



def login(request):

    return render(request, "Login/login.html")


def registro(request):


    titulo = "Registro"
    form = RegForm(request.POST or None)

    context = {
        "titulo": titulo,
        "form": form,
    }

    if form.is_valid():
        form.save()

        context = {
             "titulo": "Gracias por registrarte" ,
        }

        return redirect('/dashboard/')

    return render(request, "Login/registro.html",context)
