from django import forms

# class FonosForm(forms.Form):
#     Usuario= forms.CharField(max_length=50)
#     Anexo= forms.CharField(max_length=50)
#     Celular= forms.CharField(max_length=50)
#     IdUbicacion= forms.IntegerField()
#     UsuarioNombre= forms.CharField(max_length=50)
#     UsuarioApellido= forms.CharField(max_length=50)


    
from .models import CustomUser

class CustomUserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmar contraseña', widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ['username', 'email',  'celular', 'ubicacion', 'usuario_nombre', 'usuario_apellido']

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Las contraseñas no coinciden.")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user