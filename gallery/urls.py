from django.urls import path
from .views import CreatePostV, HomePageV


urlpatterns = [
  path("", HomePageV.as_view(), name='home'),
  path("post/", CreatePostV.as_view(), name='add_post'),
]