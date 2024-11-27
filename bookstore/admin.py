from django.contrib import admin
from .models import Book, Author, Comment


class CommentInline(admin.TabularInline):  # نمایش کامنت‌ها به صورت جدولی
    model = Comment
    extra = 0  # جلوگیری از نمایش فرم‌های خالی
    readonly_fields = ('user', 'content', 'created_at')  # فقط خواندنی برای فیلدهای مهم
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year', 'price', 'quantity')  # فیلدهای قابل نمایش در لیست
    list_filter = ('author', 'publication_year', 'price')  # فیلتر برای فیلدها
    search_fields = ('title', 'author__user__username')  # جستجو بر اساس عنوان و نویسنده
    inlines = [CommentInline]  # اضافه کردن کامنت‌ها به صورت Inline
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('user', 'bio')  # فیلدهای قابل نمایش
    search_fields = ('user__username', 'bio')  # جستجو بر اساس کاربر و بیوگرافی
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('book', 'user', 'text', 'created_at')  # فیلدهای قابل نمایش
    list_filter = ('book', 'user', 'created_at')  # فیلتر برای کامنت‌ها
    search_fields = ('content', 'user__username', 'book__title')  # جستجو
