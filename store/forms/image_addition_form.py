import fileinput
from tkinter import Widget
from store.models.image import Image
from django import forms

class ImageAdditionForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['image']
        widgets = {
            'image':forms.FileInput(attrs={'multiple':True})
        }