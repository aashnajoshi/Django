from django.contrib import admin
from tinymce.widgets import TinyMCE
from django.db import models
from .models import *

class FormAdmin(admin.ModelAdmin):
    formfield_overrides = {models.TextField: {'widget': TinyMCE()},}

admin.site.register(Form, FormAdmin)