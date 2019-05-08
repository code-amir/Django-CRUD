from django.contrib import admin
from django.urls import path
from login import views
from django.conf.urls import url, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('login/',include('login.urls')),
    path('',include('django.contrib.auth.urls')),
    path('logout/',views.user_logout,name="logout"),
    path('posts/',include('posts.urls')),
]
