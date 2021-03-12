"""appturismo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from apps.Administrar import views as vAdmin
from apps.Busqueda import views as vBusqueda
from apps.Chat import views as vChat
from apps.Contacto import views as vContact
from apps.LogIn import views as vLogin
from apps.Lugar import views as vLugar
from apps.Menu import views as vMenu
from apps.Principal import views as vMain


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',vMain.inicio,name="inicio"),
    path('login/',vLogin.login,name="login"),
    path('registro/',vLogin.registro,name="registro"),
    path('dashboard/',vAdmin.dashboard,name="dashboard"),
    path('logout/',vMain.cerrarSesion,name="logout"),
]
