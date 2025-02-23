from django.contrib import admin
from unfold.admin import ModelAdmin
# from tinymce.widgets import TinyMCE
from unfold.contrib.forms.widgets import WysiwygWidget
from .models import *

@admin.register(Form)
class CustomAdminClass(ModelAdmin):
    formfield_overrides = {models.TextField: {"widget": WysiwygWidget}}