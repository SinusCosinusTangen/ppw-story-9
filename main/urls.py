from django.urls import path

from . import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='main'),
    path('register/', views.register, name='register'),
    path('logout/', views.logOut, name = 'logout'),
    path('data', views.data, name='data'),
]