from django.urls import path
from .views import BookCreateView, BookUpdateView, BookDeleteView, book_detail_view, BookListView

urlpatterns = [
    path('book/create/', BookCreateView.as_view(), name='book_create'),
    path('book/<int:pk>/update/', BookUpdateView.as_view(), name='book_update'),
    path('book/<int:pk>/delete/', BookDeleteView.as_view(), name='book_delete'), 
    path('book/<int:pk>/', book_detail_view, name='book_detail'),
    path('books/', BookListView.as_view(), name='book_list'),
# Add this line
    # Add other URLs like book_list
]
