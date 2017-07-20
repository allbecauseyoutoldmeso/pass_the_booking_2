from django import forms
from .models import Client, Property

class ClientForm(forms.ModelForm):

    class Meta:
        model = Client
        fields = ('name', 'dob', 'email', 'telephone',)

class PropertyForm(forms.ModelForm):

    class Meta:
        model = Property
        fields = ('address', 'price', 'bedrooms', 'internet',)
