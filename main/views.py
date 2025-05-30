from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')

def membership(request):
    return render(request, 'membership.html')

def programs(request):
    return render(request, 'programs.html')

def coaches(request):
    return render(request, 'coaches.html')

def news(request):
    return render(request, 'news.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def custom_404(request, exception):
    return render(request, '404.html', status=404)
