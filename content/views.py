from django.shortcuts import render
from .models import SubCategory
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