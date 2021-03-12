from django import forms

from .models import Usuario

class RegForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ["nombre","apellido","fechaNacimiento","email","telefono","password"]
        #fields = ["nombre", "email", "password"]

        widgets={
            'password':forms.PasswordInput(),
            'fechaNacimiento':forms.DateTimeInput

        }

    def clean_nombre(self):
        nombre = self.cleaned_data.get("nombre")
        return nombre

    def clean_email(self):
        email = self.cleaned_data.get("email")
        return email


class LoginForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ["email","password"]

        widgets = {
            'password': forms.PasswordInput(),
        }

    def clean_password(self):
        password = self.cleaned_data.get("password")
        return password

    def clean_email(self):
        email = self.cleaned_data.get("email")
        return email

    def ok(self):
        return self

