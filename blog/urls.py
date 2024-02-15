from django.urls import path
from blog import views

urlpatterns = [
    path('', views.blog, name='blog'),
    path('create/', views.create_blog, name='create_blog'),
    path('<int:blog_id>/', views.read_blog, name='read_blog'),
    path('<int:blog_id>/update/', views.update_blog, name='update_blog'),
    path('<int:blog_id>/delete/', views.delete_blog, name='delete_blog'),
    path('about/', views.about, name='about')
]