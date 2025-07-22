from django.urls import path
from .import views

urlpatterns = [
    path('new/', views.post_blog, name='post_blog'),
    path('blogs', views.post_view, name='post_view'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),

]