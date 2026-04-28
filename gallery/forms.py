from django import forms
from .models import GalleryItem

class GalleryForm(forms.ModelForm):
  class Meta:
    model = GalleryItem
    fields = ['title', 'description', 'picture',] 
    