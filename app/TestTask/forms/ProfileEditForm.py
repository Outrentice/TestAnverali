from django import forms

from TestTask.models import User


class ProfileEditForm(forms.ModelForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(label='Имя', required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='Email', widget=forms.TextInput(attrs={'class': 'form-control'}))
    experience = forms.CharField(label='Опыт', required=False, widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))

    field_order = ['username', 'first_name', 'email', 'experience']

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email', 'experience')