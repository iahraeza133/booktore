 
from django.urls import path
from . import views  # از ویوهای خود برای حساب کاربری استفاده کنید
from django.contrib.auth import views as auth_views
 
 
urlpatterns = [
 
 
   
    path('signup/', views.SignupView.as_view(), name='signup'),
    ]