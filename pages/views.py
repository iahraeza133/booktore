from django.views.generic import TemplateView

# تعریف ویو صفحه اصلی با TemplateView
class HomeView(TemplateView):
    template_name = 'home.html'  # نام قالبی که می‌خواهیم رندر کنیم
