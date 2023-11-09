from django.shortcuts import render

# Create your views here.
def about(request):
    return render(request,'about.html')
def index(request):
    return render(request,'index.html')
def third(request):
    return render(request,'third.html')
def four(request):
    return render(request,'four.html')
