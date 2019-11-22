from django import forms
from .models import *

# contact form
class ContactForm(forms.Form):
    contact_name = forms.CharField(required=True , max_length= 20)
    contact_email = forms.CharField(required=True , max_length=50)
    content = forms.CharField(required=True , max_length= 500)

