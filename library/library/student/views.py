from django.shortcuts import render, redirect, render
from django.http import HttpResponse
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from student.forms import EditUserDetailsForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.utils import timezone
from books.models import Books
from student.models import Students
# Create your views here.

def showDashboard(request):
    return render(request, "student/dashboard.html")

class ListBooks(ListView):
    model = Books
    template_name = 'student/books.html'
    context_object_name = 'books'


def user_details(request):
    user = request.user
    return render(request, 'student/profile.html', {'user': user})

def edit_user_details(request):
    user = request.user
    form = EditUserDetailsForm(instance=user)
    if request.method == 'POST':
        form = EditUserDetailsForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            # Redirect to the dashboard page.
            return redirect('student.profile')
        else:
            return HttpResponse('Invalid data')

    return render(request, 'student/edit.html', {
    'form': form,
    })

# view book details

class ViewBook(DetailView):
    model = Books
    template_name = 'student/details.html'
    context_object_name = 'book'

def borrow_book(request,book_id):
    book = Books.objects.get(id=book_id)
    student = Students.objects.get(id=request.user.id)
    if book.borrowed_by is not None:
        return HttpResponse("Book already borrowed")
    
    book.borrowed_by = student
    book.borrow_date = timezone.now()
    book.save()
    return redirect('student.books')


def borrowed_books(request):
    user = request.user
    books = Books.objects.filter(borrowed_by=user)
    return render(request, 'student/borrowed.html', {'books': books})


def return_book(request, book_id):
    print("return book")
    book = Books.objects.get(id=book_id)
    
    student = Students.objects.get(id=request.user.id)
    if book.borrowed_by != student:
        return HttpResponse("You did not borrow this book")
    book.borrowed_by = None
    book.borrow_date = None
    book.save()
    return redirect('student.borrowed')