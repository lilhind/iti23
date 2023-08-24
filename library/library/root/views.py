from django.shortcuts import render, redirect
# Create your views here.

def root(request):
    # check if user is logged in
    if request.user.is_authenticated:
        return redirect('student.dashboard')
    else:
        return render(request, 'root/root.html')