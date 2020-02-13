from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from .forms import ProductForm, RawProductForm

from .models import Product

# Create your views here.

def product_list_view(request):
    queryset = Product.objects.all()#list of objects
    context = {
        "object_list": queryset
    }
    return render(request, "products/product_list.html",context)

def product_update_view(request, id=id):
    obj = get_object_or_404(Product, id=id)
    form = ProductForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
    context = {
        'form': form
    }
    return render(request, "products/product_create.html", context)


def product_delete_view(request, id):
    obj = get_object_or_404(Product, id=id)
    # POST request
    if request.method == "POST":
        #confirm delete
        obj.delete()
        return redirect('../../')
    context = {
        "object": obj
    }
    return render(request, "products/product_delete.html",context)

def dynamic_lookup_view(request,id):
    # obj = Product.objects.get(id=id)
    # obj = get_object_or_404(Product,id=id)
    try:
        obj = Product.objects.get(id=id)
    except Product.DoesNotExist:
        raise Http404
    context = {
        "object": obj
    }
    return render(request, "products/product_create.html", context)



def render_initial_data(request):
    inidital_data = {
        'title': "This is my awesome title",
        'description':"bla"
    }
    obj = Product.objects.get(id=1)
    form = RawProductForm(request.POST or None, inidital_data, instance=obj)
    if form.is_valid():
        form.save()
    context = {
        'form': form
    }
    return render(request, "products/product_create.html", context)
     


# 3
# def product_create_view(request):
#     my_form = RawProductForm()
#     if request.method == "POST":
#         my_form = RawProductForm(request.POST)
#         if my_form.is_valid():
#             #now the data is good
#             print(my_form.cleaned_data)
#             Product.objects.create(**my_form.cleaned_data)
#         else:
#             print(my_form.erros)
#     context = {
#         "form": my_form
#     }
#     return render(request, "products/product_create.html", context)

# #2
# # def product_create_view(request):
# #     #print(request.GET['title'])
# #     #print(request.POST)
# #     if request.method == 'POST':
# #         my_new_title=request.POST.get('title')
# #         print(my_new_title)
# #         #Product.objects.create(title=my_new_title)
# #     context = {}
# #     return render(request, "products/product_create.html", context)


#1
def product_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm()
        
    context = {
        'form': form
    }
    return render(request, "products/product_create.html", context)
    #return render(request, "product/detail.html", context)


def product_detail_view(request):
    obj = Product.objects.get(id=1)
    # context = {
    #     'title': obj.title,
    #     'description':obj.description
    # }
    context = {
        'object': obj
    }
    return render(request, "products/product_detail.html", context)
    #return render(request, "product/detail.html", context)
