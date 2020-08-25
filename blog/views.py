from django.shortcuts import render , HttpResponse , get_object_or_404
from blog.models import Article , Category
from django.core.paginator import Paginator


def home(request , page=1):
    article_list = Article.objects.published()
    paginator = Paginator(article_list, 2)
    # page = request.GET.get('page')
    articles = paginator.get_page(page)
    context = {
        "article": articles,
        "category": Category.objects.filter(status=True)
        
    }
    return render(request, 'blog/home.html', context)

def detail(request , slug):
    context = {
        "article": get_object_or_404(Article, slug=slug , status="p")
    }
    return  render(request, 'blog/detail.html', context)

def category(request , slug  , page=1 ):
    category = get_object_or_404(Category, slug=slug , status=True)
    article_list =  category.articles.published()
    paginator = Paginator(article_list, 2)
    articles = paginator.get_page(page)
    context = {
        "category": category,
        "article": articles
    }
    return  render(request, 'blog/category.html', context)