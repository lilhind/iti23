from django.urls import path
from django.contrib.auth.decorators import login_required
from student.views import showDashboard, ListBooks, user_details, edit_user_details, ViewBook, borrow_book, borrowed_books, return_book

urlpatterns = [
    path('', login_required(showDashboard), name='student.dashboard'),
    path('books/', login_required(ListBooks.as_view()), name='student.books'),
    path('profile/', login_required(user_details), name='student.profile'),
    path('profile/edit/', login_required(edit_user_details), name='student.edit'),
    path('books/<int:pk>/', login_required(ViewBook.as_view()), name='student.details'),
    path('books/<int:book_id>/borrow/', login_required(borrow_book), name='student.borrow'),
    path('borrowed/', login_required(borrowed_books), name='student.borrowed'),
    path('books/<int:book_id>/return/', login_required(return_book), name='book.return'),
]