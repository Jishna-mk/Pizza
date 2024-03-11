from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import UserProfile,Feedback

class UserAddForm(UserCreationForm):
    class Meta:
        model =User
        fields=["first_name" ,"username","email","password1","password2"]


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name', 'email','phone_number', 'address', ]


from django import forms

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['content']
