from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm

from .models import *




class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__'


# class CreateUserForm(UserCreationForm):
#     class Meta:
#         model = User
#         fields = ['username','email','password1','password2']
