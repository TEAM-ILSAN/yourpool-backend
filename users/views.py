from django.shortcuts import render

def empty(request):
    return render(request, 'users/empty.html')
