from django import forms
from django.contrib.auth.forms import UserCreationForm
from simplemooc.apps.courses.models import Course
from django.contrib.auth import get_user_model
from simplemooc.apps.core.mail import send_mail_template
from simplemooc.apps.core.utils import generate_hash_key
from .models import PasswordReset
from django.conf import settings

User = get_user_model() #Indica pro django que vou usar o meu Custom User

class PasswordResetForm(forms.Form):
    email = forms.EmailField(label='E-mail')

    #Verifica se já existe o email cadastrado
    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            return email
        raise forms.ValidationError('Nenhum usuário encontraodo com esse e-mail')

    def save(self):
        user = User.objects.get(email = self.cleaned_data['email']) #busca o usuário do email
        key = generate_hash_key(user.username) #Gera a chave
        reset = PasswordReset(key=key, user=user) #chama o model de reset de senha
        reset.save()
        template_name = 'accounts/password_reset_email.html'
        subject = 'Redefinição de senha SimpleMooc'
        context = {
            'reset':reset
        }
        send_mail_template(subject, template_name, context, [user.email])

class RegisterForm(forms.ModelForm): #Herda de UserCreationForm
    password1 = forms.CharField(label='Senha', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmação de Senha', widget=forms.PasswordInput)

    #Verifica se as digitadas são iguais
    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('A confirmação da senha está incorreta')
        return password2

    #Função para salvar o email no banco de dados
    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password1']) #set_password, criptografa a senha
        if commit:
            user.save()
        return user

    class Meta:
        model = User
        fields = ['image','name','username', 'email']

class EditAccountForm(forms.ModelForm): #ModelForm pega os campos do form

    def clean_email(self):
        email = self.cleaned_data['email']
        queryset =  User.objects.filter(email=email).exclude(pk=self.instance.pk)
        if queryset.exists():
            raise forms.ValidationError('E-mail já cadastrado!')
        return email

    class Meta:
        model = User #Form que o modelForm vai pegar  os compos
        fields = ['name','username', 'email','image'] #Campos que serão importados


'''Variável instance todo ModelForm tem, e ele indica que estou alterando a instância 
atual do modelo que está sendo editado, ou seja, o usuário logado'''

class AddCoursesForm(forms.ModelForm):

    class Meta:
        model = Course
        fields = ['name','slug','description','about','start_date', 'image']