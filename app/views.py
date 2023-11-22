from django.shortcuts import render

# Create your views here.

def something(request):
    return render(request,'something.html')