from django import forms
from .models import Car, Person, Rent, User
from django.core.validators import RegexValidator
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm


class UserForm(UserCreationForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()

    class Mata:
        model = User


class SomeWidget(forms.TextInput):
    input_type = "date"


class CarForm(ModelForm):

    class Meta:
        model = Car
        exclude = ["renters"]
        fields = "__all__"


class PersonForm(ModelForm):
    class Meta:
        model = Person
        exclude = ["user"]
        fields = "__all__"


class RentForm(ModelForm):
    end_date = forms.DateTimeField(required=False,
                                   widget=forms.DateTimeInput(attrs={'type': 'datetime-local',
                                                                     }),
                                   label='end date')

    class Meta:
        model = Rent
        exclude = ["blala"]
        fields = "__all__"


class LoginForm(forms.Form):
    username = forms.CharField(required=True, max_length=50)
    password = forms.CharField(required=True, max_length=50)
