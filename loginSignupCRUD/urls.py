from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.signupPage, name='signupPage'),
    path('loginPage/', views.loginPage, name='loginPage'),
    path('index/', views.index, name='index'),
]
