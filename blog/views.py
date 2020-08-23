from django.shortcuts import render , HttpResponse
from blog.models import Article



def home(request):
    context = {
        "article": Article.objects.all()
    }
    return render(request, 'blog/home.html', context)

def detail(request , slug):
    context = {
        "article": Article.objects.get(slug=slug)
    }
    return render(request, 'blog/detail.html', context)