from django import forms
from django.contrib.auth.forms import UserCreationForm

from TestTask.models import User


class RegisterForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='Email', widget=forms.TextInput(attrs={'class': 'form-control'}))
    role = forms.ChoiceField(
        label='Роль', choices=(('Фрилансер', 'Фрилансер'), ('Заказчик', 'Заказчик')),
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    field_order = ['username', 'email', 'role', '<PASSWORD>', '<PASSWORD>']

    class Meta:
        model = User
        fields = ('username', 'email', 'role', 'password1', 'password2')