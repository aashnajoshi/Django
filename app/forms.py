from django import forms
from django.utils import timezone
from .models import Form
# from tinymce.widgets import TinyMCE

class FormEntry(forms.ModelForm):
    class Meta:
        model = Form
        fields = ['name', 'email', 'dob', 'img', 'doc', 'choice', 'message', 'date_added']
        widgets = {
            'dob': forms.DateInput(attrs={'type': 'date'}),
            'date_added': forms.DateInput(attrs={'type': 'date', 'disabled': True}),
            'message': forms.Textarea(attrs={'cols': 40, 'rows': 3}),
            # 'message': TinyMCE(attrs={'cols': 40, 'rows': 3}),
        }

    def __init__(self, *args, **kwargs):
        super(FormEntry, self).__init__(*args, **kwargs)
        self.fields['date_added'].initial = timezone.now().date()
        self.fields['date_added'].required = False