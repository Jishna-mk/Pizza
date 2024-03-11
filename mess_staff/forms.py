from django.forms import ModelForm
from django import forms
from .models import FoodItem



class FoodItemForm(forms.ModelForm):
    class Meta:
        model = FoodItem
        fields = ['name', 'image', 'price', 'quantity_available']


from django import forms
from .models import AdminNotification

class AddNotificationForm(forms.ModelForm):
    class Meta:
        model = AdminNotification
        fields = ['title', 'message']
