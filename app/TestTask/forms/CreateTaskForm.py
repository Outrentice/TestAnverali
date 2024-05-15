from django import forms

from TestTask.models import Order


class CreateTaskForm(forms.ModelForm):
    name = forms.CharField(label='Заголовок', widget=forms.TextInput(attrs={'class': 'form-control'}))
    description = forms.CharField(label='Описание', widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Order
        fields = ('name', 'description')