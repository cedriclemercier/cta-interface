# forms.py
from django import forms
from .models import Image
from multiupload.fields import MultiFileField

class ImageUploadForm(forms.Form):
    attachments = MultiFileField(min_num=1, max_num=100)