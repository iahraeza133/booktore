from django.db import models
from django.conf import settings  # برای دسترسی به AUTH_USER_MODEL
from django.urls import reverse
# مدل نویسنده
from django.contrib import admin
from django.contrib.auth import get_user_model  
class Comment(models.Model):
    book = models.ForeignKey('Book', on_delete=models.CASCADE,related_name='comments')  # ارتباط با مدل Book
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # ارتباط با مدل کاربر
    content = models.TextField(help_text="متن کامل نظر")
    created_at = models.DateTimeField(auto_now_add=True)  # زمان ثبت نظر
    text = models.CharField(max_length=255, blank=True, help_text="خلاصه نظر یا عنوان")  # اختیاری
    is_active=models.BooleanField(default=True)
    


class Author(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # استفاده از AUTH_USER_MODEL
    bio = models.TextField(blank=True, null=True)  # بیوگرافی نویسنده

    def __str__(self):
        return self.user.username  # نمایش نام کاربری نویسنده به جای name

# مدل کتاب
class Book(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)  # ارتباط با مدل Author
    publication_year = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=3, default='USD')
    quantity = models.IntegerField()
   
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        # Redirect to the book detail page after creation
         return reverse('book_detail', kwargs={'pk': self.pk})
from django.conf import settings
from django.db import models
