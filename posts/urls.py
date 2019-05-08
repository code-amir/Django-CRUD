from django.conf.urls import url
from posts import views
from django.urls import path

app_name = 'posts'

urlpatterns = [
    path('home/',views.home,name='home'),
    path('createPost/',views.createPost,name='createPost'),
    path('listPost/',views.listPost,name='listPost'),
]
