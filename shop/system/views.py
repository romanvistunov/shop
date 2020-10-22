from django.shortcuts import render
from django.http import HttpResponse
from catalog.models import Product
from django.db.models import Q
from catalog.models import Product
from django.http import JsonResponse
import simplejson as json
from django.core import serializers


def index(request):
    context = {}
    template = 'system/index.html'
    return render(request, template, context)

def global_search(request):
    query = request.GET.get('text')
    search_results = Product.objects.filter(Q(name__icontains=query))
    context = {'search_results':search_results}
    template = 'system/search_results.html'
    return render(request, template, context)

def validate_product(request):
    product = request.GET.get('product', None)
    query = Product.objects.filter(name__iexact=product)
    data = {
        'is_taken': Product.objects.filter(name__iexact=product).exists(),
    }
    return HttpResponse(json.dumps(data))


def filter_products(request):
    ordering = request.GET.get('ordering', None)
    if ordering == "price_dec":
        qset = Product.objects.filter(available=True).order_by('-price')
    if ordering == "price_inc":
        qset = Product.objects.filter(available=True).order_by('price')
    
    data = {'qset': serializers.serialize('json', list(qset))}
    return HttpResponse(json.dumps(data))
