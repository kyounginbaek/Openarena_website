from django.shortcuts import render

def home(request):
    return render(request, 'main/home.html', {})

def looking(request):
    return render(request, 'main/looking.html', {})

def making(request):
    return render(request, 'main/making.html', {})

def video(request):
    return render(request, 'main/video.html', {})

def hallfame(request):
    return render(request, 'main/hallfame.html', {})

def login(request):
    return render(request, 'main/login.html', {})
