from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy

from .models import GalleryItem
from .forms import GalleryForm

# Create your views here.
class HomePageV(ListView):
  model = GalleryItem
  template_name = "gallery/home.html"
  
class CreatePostV(CreateView):
  model = GalleryItem
  form_class = GalleryForm
  template_name = "gallery/post.html"
  success_url = reverse_lazy('home')

class EditPostV(UpdateView):
  model = GalleryItem
  form_class = GalleryForm
  template_name = "gallery/edit_post.html"
  success_url = reverse_lazy('home')