from django.shortcuts import render
from .models import SubCategory
# Create your views here.

def home(request):
    if request.method == 'GET':
        subs = SubCategory.objects.all()
        def list_generator(subs, parent = None):
            lst = []
            for sub in subs:
                if sub.inner_sub_id == parent:
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

