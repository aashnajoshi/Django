from django import forms
from .models import FormEntry

class FormEntryForm(forms.ModelForm):
    class Meta:
        model = FormEntry
        fields = ['name', 'email', 'dob', 'img', 'doc', 'choice', 'message', 'date_added']