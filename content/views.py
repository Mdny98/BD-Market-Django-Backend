from django.shortcuts import render
from .models import SubCategory, Product, Attribute
from Supplier.models import ProductSupplier
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

def get_parent_cats(cat):
    catlst = []
    f = 1
    catlst.append(cat)
    while f:
        catlst.append(cat.parent_category)
        cat = cat.parent_category
        if cat.parent_category == None:
            f = 0
    catlst.reverse()
    return catlst
    

def products(request, cat_pk):
    if request.method == 'GET':
        all_products = Product.objects.filter(subcategory_id=cat_pk)
        q = all_products
        print(request.GET)
        for k, v in request.GET.items():
            tmpq = Attribute.objects.get(attr_title=k)
            qtype = tmpq.pro_attr.all()[0].value_type
            print(f'\nqtype is {qtype}')
            if qtype == 'BOOL':
                q = q.filter(pro_attr__attr_id__attr_title=k, pro_attr__bool_value=v)
            elif qtype == 'INT':
                q = q.filter(pro_attr__attr_id__attr_title=k, pro_attr__int_value=v)
            elif qtype == 'TXT':
                q = q.filter(pro_attr__attr_id__attr_title=k, pro_attr__text_value=v)

            # print(f'\nk is {k}')
            # print(f'\nk type is {type(k)}')
            # print(f'\nq is {q}')

        cat = SubCategory.objects.get(pk=cat_pk)
        catlst = get_parent_cats(cat)
        return render(request, 'content/products.html', 
            {'all_products':q, 'catlst':catlst, 'cat':cat})


def productdetails(request, product_pk):
    if request.method == 'GET':
        this_product = Product.objects.get(pk=product_pk)
        this_product_suppliers = ProductSupplier.objects.filter(product_id=this_product)
        cat = this_product.subcategory_id
        catlst = get_parent_cats(cat)
        return render(request, 'content/productdetails.html', 
        {'this_product':this_product, 'catlst':catlst, 'this_product_suppliers':this_product_suppliers})