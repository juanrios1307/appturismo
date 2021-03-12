from django.shortcuts import render
from django.urls import reverse

#from ..LogIn.views import registro

# Create your views here.

#reverse(registro())

def dashboard(request):

    registroMsg = request.session.get('registroMsg')
    registroBool=request.session.get('registroBool')

    loginMsg = request.session.get('loginMsg')
    loginBool = request.session.get('loginBool')

    email = request.session.get('login')

    context = {
        'context': "Hola",
        'email':email
    }

    if(registroBool == True):
        context = {
            'context': registroMsg
        }
        request.session['registroBool'] = False
        del request.session['registroMsg']

    if(loginBool == True):
        context = {
            'context': loginMsg
        }
        request.session['loginBool'] = False
        del request.session['loginMsg']

    #del request.session['registro']

    return render(request, "Administrar/Dashboard.html",context)
