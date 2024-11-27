"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.contrib import admin
from django.urls import path, include
# urls.py
from django.contrib.auth import views as auth_views

from django.contrib import admin
from django.urls import path, include
import debug_toolbar

urlpatterns = [
    path('admin/', admin.site.urls),  # مسیر برای پنل مدیریت
    path('accounts/', include('accounts.urls')),  # مسیر برای اپلیکیشن accounts (مثلاً ثبت‌نام و ورود)
    path('accounts/', include('django.contrib.auth.urls')),  # مسیرهای پیش‌فرض Django برای ورود و خروج
    path('pages/', include('pages.urls')), 
    path("bookstore/",include('bookstore.urls')),# مسیر برای اپلیکیشن pages

    path('__debug__/', include(debug_toolbar.urls)),  # اضافه کردن URL دیباگ تولبار
]
