from django.contrib import admin

# Register your models here.
from .forms import RegForm
from .models import Usuario


class AdminRegistrado(admin.ModelAdmin):
    list_display = ["email","nombre","apellido","fechaNacimiento","telefono","password","timestamp"]
    form = RegForm
    # list_display_links = ["email"]
    list_filter = ["timestamp"]
    list_editable = ["nombre"]
    search_fields = ["email", "nombre"]
    # class Meta:
    #   model=Registrado


admin.site.register(Usuario,AdminRegistrado)