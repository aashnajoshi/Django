from django.contrib import admin
from unfold.admin import ModelAdmin
# from tinymce.widgets import TinyMCE
from unfold.contrib.forms.widgets import WysiwygWidget
from unfold.contrib.import_export.forms import (ExportForm, ImportForm, SelectableFieldsExportForm)
from .models import *

@admin.register(Form)
class CustomAdminClass(ModelAdmin):
    formfield_overrides = {models.TextField: {"widget": WysiwygWidget}}
    import_form_class = ImportForm
    export_form_class = ExportForm
    selectable_export_form_class = SelectableFieldsExportForm