from django import forms

from .models import Usuario

class RegForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ["nombre","email","password"]
        widgets={
            'password':forms.PasswordInput(),
        }

    def clean_nombre(self):
        nombre = self.cleaned_data.get("nombre")
        return nombre


class LoginForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ["email","password"]

    def ok(self):
        return self

