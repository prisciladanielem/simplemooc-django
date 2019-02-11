from django import forms

from django.contrib.auth.forms import UserCreationForm

class RegisterForm(UserCreationForm): #Herda de UserCreationForm
    email = forms.EmailField(label = 'E-mail')

    #Função para salvar o email no banco de dados
    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user