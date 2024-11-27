from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm

class CustomUserAdmin(UserAdmin):
    # فرم ایجاد کاربر جدید
    add_form = CustomUserCreationForm

    # فرم ویرایش کاربر
    form = CustomUserChangeForm

    # مدل مربوطه
    model = CustomUser

    # فیلدهایی که در پنل مدیریت نمایش داده می‌شوند
    list_display = ['username', 'email', 'first_name', 'last_name', 'birth_date',  'is_staff']

    # فیلدهایی که در فرم ویرایش نمایش داده می‌شوند
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'birth_date',)}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

    # فیلدهایی که در فرم افزودن کاربر نمایش داده می‌شوند
    add_fieldsets = (
        (None, {'fields': ('username', 'email', 'password1', 'password2')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'birth_date',)}),
    )

    # فیلدهای قابل فیلتر در پنل مدیریت
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')

    # جستجو در فیلدهای خاص
    search_fields = ('username', 'email', 'first_name', 'last_name')

    # نمایش تعداد کاربران در هر صفحه
    ordering = ('username',)

# ثبت مدل CustomUser با تنظیمات جدید
admin.site.register(CustomUser, CustomUserAdmin)
