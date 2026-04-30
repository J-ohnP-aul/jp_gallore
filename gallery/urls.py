from django.urls import path
from .views import CreatePostV, HomePageV, EditPostV


urlpatterns = [
  path("", HomePageV.as_view(), name='home'),
  path("post/", CreatePostV.as_view(), name='add_post'),
  path('edit/<int:pk>/', EditPostV.as_view(), name='edit_post')
]