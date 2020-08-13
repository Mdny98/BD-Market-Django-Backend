from django.shortcuts import render
from .models import SubCategory, Product
# Create your views here.

def home(request):
    if request.method == 'GET':
        subs = SubCategory.objects.all()
        def list_generator(subs, parent = None):
            lst = []
            for sub in subs:
                if sub.parent_category == parent:
                    lst.append(sub)
                    tmp = list_generator(subs, sub)
                    if tmp:
                        lst.append(tmp)
            return lst
        lst = list_generator(subs)
        print(f'list is {lst}')
        return render(request, 'content/home.html', {'subs':lst})
    else:
        pass

def categories(request):
    if request.method == 'GET':
        all_cats = SubCategory.objects.all()
        main_cats = all_cats.filter(parent_category = None)
        return render(request, 'content/categories.html', {'all_cats':all_cats, 'main_cats':main_cats})

def products(request, cat_pk):
    if request.method == 'GET':
        all_products = Product.objects.filter(subcategory_id=cat_pk)
        cat = SubCategory.objects.get(pk=cat_pk)
        print(cat)
        return render(request, 'content/products.html', {'all_products':all_products, 'cat':cat})
