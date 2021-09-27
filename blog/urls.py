from django.urls import path
from .views import HomeView, CreatePostView, PostDetailsView,PostUpdateView,PostDeleteView
app_name = "blog"
urlpatterns = [
    path('',HomeView.as_view(), name='home'),
    path('create/',CreatePostView.as_view(), name='create'),
    path('<int:pk>',PostDetailsView.as_view(),name='details'),
    path('<int:pk>/update/',PostUpdateView.as_view(),name='update'),
    path('<int:pk>/delete/',PostDeleteView.as_view(),name='delete')
]
