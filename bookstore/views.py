from django.shortcuts import render
from django.views import generic
from .models import Book  # Import your model
from django.views.generic import DetailView
from django.urls import reverse_lazy
from django.views import generic
from .models import Book
from django.shortcuts import render, get_object_or_404, redirect
from . forms import Commentform
from django.views.generic import ListView,CreateView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin#مهم
class BookCreateView(LoginRequiredMixin, generic.CreateView):
    model = Book  # Specify the model you're working with
    template_name = 'bookstore/book_create.html'  # Specify the template for the form
    fields = ['title', 'author','price', 'publication_year','quantity']  # Add the fields you want to display in the form

class BookUpdateView(LoginRequiredMixin,UserPassesTestMixin,generic.UpdateView):
    model = Book  # Specify the model you're working with
    template_name = 'bookstore/book_update.html'  # Specify the template for the form
    fields = ['title', 'author', 'price']  # Add the fields you want to display in the form
    success_url = reverse_lazy('book_list')
    
    def test_func(self):
        obj=self.get_object()
        return obj.user==self.request.user
    
    #
    #اگر خروجی ترو شود کاربر حق دسترسی ب صفحه را دارد#
    
    
    
    
    # Redirect to the book list after updating a book
    


class BookDeleteView(generic.DeleteView):
    model = Book  # Specify the model you're working with
    template_name = 'bookstore/book_delete.html'  # Specify the template for the confirmation page
    success_url = reverse_lazy('book_list')  # Redirect to the book list after deleting a book
# class BookDetailView(DetailView):
#     model = Book
    
#     template_name = 'bookstore/book_details.html'
#     context_object_name = 'book'  # The context variable name to access the b
    
class BookListView(ListView):
    model = Book
   
    template_name = 'bookstore/book_list.html'  # Specify the template to use
    context_object_name = 'books'  # The name of the context variable in the template
    paginate_by = 10  #
    
    
from django.shortcuts import render, get_object_or_404
from .models import Book, Comment
from .forms import Commentform  # فرض می‌کنیم نام فرم شما CommentForm است







from django.contrib.auth.decorators import login_required

@login_required #for functional view to login required
def book_detail_view(request, pk):
    # دریافت کتاب با pk مشخص
    book = get_object_or_404(Book, pk=pk)
    comments = book.comments.all()  # گرفتن تمام کامنت‌های مرتبط با این کتاب
#هندل کردن فرم###########################################################
    if request.method == 'POST':
        if request.method == 'POST':
        # ایجاد فرم از داده‌های ارسال شده
            comment_form = Commentform(request.POST)
            
            # بررسی اینکه فرم معتبر است
            if comment_form.is_valid():
                # ذخیره کردن کامنت جدید
                new_comment = comment_form.save(commit=False)
                new_comment.book = book  # اختصاص کتاب به کامنت
                new_comment.user = request.user  # اختصاص کاربر به کامنت
                new_comment.save()  # ذخیره کامنت

                # بعد از ذخیره کامنت، هدایت به صفحه کتاب با کامنت‌های جدید
                return redirect('book_detail', pk=book.pk)
    else:
        # در صورتی که درخواست GET باشد، فرم خالی نمایش داده می‌شود
        comment_form = Commentform()
###############################################################################################
    return render(request, 'bookstore/book_details.html', {
        'book': book,
        'comments': comments,
        'comment_form': comment_form  # ارسال فرم به قالب
    })
