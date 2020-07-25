from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('post', views.post, name='post'),
    path('comments', views.comment, name='comments'),
    path('about', views.about, name='about')
]