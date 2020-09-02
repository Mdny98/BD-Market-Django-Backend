from django.shortcuts import render,  HttpResponse, redirect
from django.template.defaulttags import register
from django.db.models import Q
from django.views.generic.base import View
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import SubCategory, Product, Attribute
from Supplier.models import ProductSupplier
from .forms import CommentForm
# Create your views here.


@register.filter
def get_item(dictionary, key):
    res = str(dictionary.get(key)[0])
    return res


def home(request):
    if request.method == 'GET':
        subs = SubCategory.objects.all()

        def list_generator(subs, parent=None):
            lst = []
            try:
                for sub in subs:
                    if sub.parent_category == parent:
                        lst.append(sub)
                        tmp = list_generator(subs, sub)
                        if tmp:
                            lst.append(tmp)
                return lst
            except:
                return HttpResponse('hi')
        lst = list_generator(subs)
        # print(f'list is {lst}')
        return render(request, 'content/home.html', {'subs': lst})
    else:
        pass


def categories(request):
    if request.method == 'GET':
        all_cats = SubCategory.objects.all()
        main_cats = all_cats.filter(parent_category=None)
        return render(request, 'content/categories.html', {'all_cats': all_cats, 'main_cats': main_cats})


def get_parent_cats(cat):
    catlst = []
    f = 1
    catlst.append(cat)
    if cat.parent_category:
        while f:
            catlst.append(cat.parent_category)
            cat = cat.parent_category
            if cat.parent_category == None:
                f = 0
    catlst.reverse()
    return catlst


def get_child_cats(cat):
    catlst = []
    f = 1
    catlst.append(cat)
    if cat.child_categories.all():
        for ccat in cat.child_categories.all():
            get_child_cats(ccat)

    return catlst


def products(request, cat_pk):


    if request.method == 'GET':
        cat = SubCategory.objects.get(pk=cat_pk)
        catlst = get_child_cats(cat)
        all_products = Product.objects.filter(subcategory_id__in=catlst)
        q = all_products
        # print(request.GET)
        for k, v in request.GET.items():
            if not k == 'page':
                tmpq = Attribute.objects.get(attr_title=k)
                qtype = tmpq.pro_attr.all()[0].value_type
                # print(f'\nqtype is {qtype}')
                if qtype == 'BOOL':
                    q = q.filter(pro_attr__attr_id__attr_title=k,
                                pro_attr__bool_value=v)
                elif qtype == 'INT':
                    q = q.filter(pro_attr__attr_id__attr_title=k,
                                pro_attr__int_value=v)
                elif qtype == 'TXT':
                    q = q.filter(pro_attr__attr_id__attr_title=k,
                                pro_attr__text_value=v)

            # print(f'\nk is {k}')
            # print(f'\nk type is {type(k)}')
            # print(f'\nq is {q}')

        page = request.GET.get('page', 1)

        paginator = Paginator(q, 1)
        try:
            q = paginator.page(page)
        except PageNotAnInteger:
            q = paginator.page(1)
        except EmptyPage:
            q = paginator.page(paginator.num_pages)


        checked_attr = dict(request.GET)
        # print(f'\n checked_attr = {checked_attr}')

        cat = SubCategory.objects.get(pk=cat_pk)
        uniqdict = dict()
        tmp = []
        attrs = cat.attr.all()
        # print(f'\nattrs is {attrs}')
        for attr in attrs:
            for proattr in attr.pro_attr.all():
                if proattr.value_type == 'BOOL':
                    tmp.append(str(proattr.bool_value))
                if proattr.value_type == 'INT':
                    tmp.append(str(proattr.int_value))
                if proattr.value_type == 'TXT':
                    tmp.append(proattr.text_value)
                uniqtmp = list(set(tmp))
            uniqdict[attr] = list(uniqtmp)
            tmp.clear()
            uniqtmp.clear()

        # print(f'\nuniqdict is {uniqdict}')
        catlst = get_parent_cats(cat)
        return render(request, 'content/products.html',
                      {'all_products': q, 'catlst': catlst, 'cat': cat, 'uniqdict': uniqdict, 'checked_attr': checked_attr})


def productdetails(request, product_pk):

    
    this_product = Product.objects.get(pk=product_pk)
    this_product_suppliers = ProductSupplier.objects.filter(
        product_id=this_product)
    cat = this_product.subcategory_id
    pro4 = Product.objects.filter(subcategory_id=cat)[:4]
    if request.method == 'GET':

        catlst = get_parent_cats(cat)
        return render(request, 'content/productdetails.html',
                        {'this_product': this_product, 'catlst': catlst,
                        'this_product_suppliers': this_product_suppliers, 'cmform': CommentForm(),
                        'pro4': pro4})
    else:
        try:
            form = CommentForm(request.POST)
            newcm = form.save(commit=False)
            newcm.custumer_id = request.user.customer
            newcm.product_id = Product.objects.get(pk=product_pk)
            newcm.save()
            return redirect('content:productdetails', product_pk)
        except ValueError:
            return render(request, 'content/productdetails.html', 
                {'this_product': this_product, 'catlst': catlst,
                'this_product_suppliers': this_product_suppliers, 'cmform': CommentForm(),
                'pro4': pro4, 'error': 'Bad data passed in!'})


class SearchProduct(View):

    def get(self, request, *args, **kwargs):
        search_text = request.GET['search']
        result = Product.objects.filter(
            Q(product_name__icontains=search_text) |
            Q(product_description__icontains=search_text)
        ).distinct()
        return render(request, 'content/search_result.html', {'search_result': result})


def error_404(request, exception):
    data = {"name": "somthing error"}
    return render(request, 'content/bdmarket404.html', data)


def error_500(request):
    data = {"name": "somthing error"}
    return render(request, 'content/bdmarket404.html', data)
