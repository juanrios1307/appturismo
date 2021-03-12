from django.shortcuts import render, redirect
from django.urls import reverse
from django.db import connection


from .forms import RegForm,LoginForm
from .models import Usuario
from ..Administrar.views import dashboard
# Create your views here.



def login(request):
    titulo = "Login"
    form = LoginForm(request.POST or None)

    context = {
        "titulo": titulo,
        "form": form,
    }


    if form.is_valid():
        email = form.clean_email()
        password = form.clean_password()

        with connection.cursor() as cursor:
            cursor.execute('SELECT id,email,password FROM LogIn_usuario WHERE email=%s AND password=%s',
                                    [email, password])
            row = cursor.fetchall()

            print(row)

            if(len(row) >= 1 ):
                request.session['loginMsg'] = "Ingreso Exitoso"
                request.session['loginBool'] = True

                request.session['login']=email

                return redirect('/dashboard/')

            else :

                context = {
                    "titulo": "Correo o contraseña incorrectas",

                }


    return render(request, "Login/login.html",context)


def registro(request):

    email = request.session.get('login')

    if email == None:
        titulo = "Registro"
        form = RegForm(request.POST or None)

        context = {
            "titulo": titulo,
            "form": form,
        }

        if form.is_valid():
            form.save()


            request.session['registroMsg']="Registro Exitoso"
            request.session['registroBool']=True
            request.session['login'] = form.clean_email()

            return redirect('/dashboard/')
    else:
        return redirect('/dashboard/')

    return render(request, "Login/registro.html",context)

