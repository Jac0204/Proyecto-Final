from django.urls import path
from login import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signin', views.index, name='signin'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.signout, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('photo_profile/', views.photo_profile, name='photo_profile'),
    path('update_password/', views.update_password, name='update_password'),
]
