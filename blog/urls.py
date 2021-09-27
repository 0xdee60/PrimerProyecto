from django.urls import path
from .views import HomeView, CreatePostView, PostDetailsView
app_name = "blog"
urlpatterns = [
    path('',HomeView.as_view(), name='home'),
    path('create/',CreatePostView.as_view(), name='create'),
    path('<int:pk>',PostDetailsView.as_view(),name='details')
]
