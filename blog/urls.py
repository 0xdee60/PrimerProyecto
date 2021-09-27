from django.urls import path
from .views import HomeView, CreatePostView
app_name = "blog"
urlpatterns = [
    path('',HomeView.as_view(), name='home'),
    path('create/',CreatePostView.as_view(), name='create')
]
