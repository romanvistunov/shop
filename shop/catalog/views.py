from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Category, Product, Gallery
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from cart.forms import CartAddProductForm



def catalog_all(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request,
                  'catalog/index.html',
                  {'category': category,
                   'categories': categories,
                   'products': products})


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
        products_len = len(products)
        paginator = Paginator(products, 100) # Show 25 contacts per page.
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

    return render(request,
                  'catalog/product_list.html',
                  {'category': category,
                   'categories': categories,
                   'products': products,
                   'products_len': products_len,
                   'page_obj': page_obj})


def product_detail(request, id, slug):
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                available=True)
    gallery = Gallery.objects.filter(product=product)
    cart_product_form = CartAddProductForm()
    return render(request, 'catalog/product_detail.html',
                  {'product': product,
                  'gallery': gallery,
                   'cart_product_form': cart_product_form})
