from django import forms

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from simplemooc.apps.courses.models import Course

class RegisterForm(UserCreationForm): #Herda de UserCreationForm
    first_name = forms.CharField(label='Primeiro nome',max_length=100)
    last_name = forms.CharField(label='Último nome',max_length=100)
    email = forms.EmailField(label = 'E-mail')

    #Função para o email ser único no cadastro
    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('E-mail já cadastrado!')
        return email

    #Função para salvar o email no banco de dados
    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        if commit:
            user.save()
        return user

class EditAccountForm(forms.ModelForm): #ModelForm pega os campos do form

    def clean_email(self):
        email = self.cleaned_data['email']
        queryset =  User.objects.filter(email=email).exclude(pk=self.instance.pk)
        if queryset.exists():
            raise forms.ValidationError('E-mail já cadastrado!')
        return email

    class Meta:
        model = User #Form que o modelForm vai pegar  os compos
        fields = ['username', 'email', 'first_name', 'last_name'] #Campos que serão importados


'''Variável instance todo ModelForm tem, e ele indica que estou alterando a instância 
atual do modelo que está sendo editado, ou seja, o usuário logado'''

class AddCoursesForm(forms.ModelForm):

    class Meta:
        model = Course
        fields = ['name','slug','description','about','start_date', 'image']