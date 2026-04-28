from django.db import models
from django.utils import timezone

# Create your models here.

class GalleryItem(models.Model):
  title = models.CharField(max_length=70)
  description = models.TextField()
  created_at = models.DateTimeField(default=timezone.now)
  picture = models.ImageField(upload_to='images/')
  
  def __str__(self):
    return self.title
  
  
  