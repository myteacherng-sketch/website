from django.shortcuts import render

def home_view(request):
    return render(request, "home.html") 

def about_view(request):
    return render(request, "about.html")

def signup(request):
    return render(request, "signup.html")

def contactUs_view(request):
    return render(request, "contactUs.html")

def blog_view(request):
    return render(request, "blog.html")