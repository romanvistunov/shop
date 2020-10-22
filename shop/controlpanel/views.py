from django.shortcuts import render, redirect, get_object_or_404
from catalog.models import Category, Product, Gallery
from .models import Client
from orders.models import Order, OrderItem
from .forms import CategoryChangeForm, ProductChangeForm, OrderChangeForm
from django.views.decorators.http import require_POST
from django.forms import inlineformset_factory
from django.contrib.admin.views.decorators import staff_member_required


@staff_member_required
def panel_index(request):
    sidebar_list = True
    template = 'cp/index.html'
    context = {'sidebar_list': sidebar_list}
    return render(request, template, context)


@staff_member_required
def category_index(request):
    categories = Category.objects.all()
    template = 'cp/category_index.html'
    context = {'categories': categories}
    return render(request, template, context)


@staff_member_required
def orders_index(request):
    orders = Order.objects.all()
    template = 'cp/orders_index.html'
    context = {'orders': orders}
    return render(request, template, context)


@staff_member_required
def products_index(request):
    products = Product.objects.all()
    template = 'cp/products_index.html'
    context = {'products': products}
    return render(request, template, context)


@staff_member_required
def clients_index(request):
    clients = Client.objects.all()
    template = 'cp/clients_index.html'
    context = {'clients': clients}
    return render(request, template, context)


@staff_member_required
def category_detail(request, id):
    alert = False
    errors = False
    category = get_object_or_404(Category, id=id)
    if request.method == 'POST':
        form = CategoryChangeForm(
            request.POST, request.FILES, instance=category)
        if form.is_valid():
            form.save()
            alert = 'success'
        else:
            alert = 'danger'
            errors = form.errors
    else:
        form = CategoryChangeForm(initial={
            'name': category.name,
            'number': category.number,
            'slug': category.slug,
            'image': category.image})
    template = 'cp/category_detail.html'
    context = {'form': form, 'category': category,
               'alert': alert, 'errors': errors}
    return render(request, template, context)


@staff_member_required
def category_delete(request, id):
    category = get_object_or_404(Category, id=id)
    if request.method == 'POST':
        Category.objects.filter(id=id).delete()
        return redirect('controlpanel:category_index')
    else:
        pass
    template = 'cp/category_delete.html'
    context = {'category': category}
    return render(request, template, context)


@staff_member_required
def category_add(request):
    alert = False
    errors = False
    if request.method == 'POST':
        form = CategoryChangeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            alert = 'success'
        else:
            alert = 'danger'
            errors = form.errors
        return redirect('controlpanel:categories_index')
    else:
        form = CategoryChangeForm(initial={'number': ''})
    template = 'cp/category_add.html'
    context = {'form': form, 'alert': alert, 'errors': errors}
    return render(request, template, context)


@staff_member_required
def product_detail(request, id):
    alert = False
    errors = False
    product = get_object_or_404(Product, id=id)
    gallery = Gallery.objects.filter(product=product)
    ProductFormSet = inlineformset_factory(Product, Gallery, fields=('image',))
    if request.method == 'POST':
        form = ProductChangeForm(request.POST, request.FILES, instance=product)
        formset = ProductFormSet(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            alert = 'success'
        else:
            alert = 'danger'
            errors = form.errors
        if formset.is_valid():
            formset.save()
            alert = 'success'
        else:
            alert = 'danger'
            errors = formset.errors
        return redirect('controlpanel:products_index')
    else:
        form = ProductChangeForm(initial={
            'category': product.category,
            'name': product.name,
            'slug': product.slug,
            'mainimage': product.mainimage,
            'description': product.description,
            'code': product.code,
            'size': product.size,
            'contents': product.contents,
            'price': product.price,
            'available': product.available,
        })
        formset = ProductFormSet(instance=product)
    template = 'cp/product_detail.html'
    context = {'form': form, 'formset': formset, 'product': product,
               'gallery': gallery, 'alert': alert, 'errors': errors, }
    return render(request, template, context)


@staff_member_required
def product_delete(request, id):
    product = get_object_or_404(Product, id=id)
    if request.method == 'POST':
        Product.objects.filter(id=id).delete()
        return redirect('controlpanel:products_index')
    else:
        pass
    template = 'cp/product_delete.html'
    context = {'product': product}
    return render(request, template, context)


@staff_member_required
def product_add(request):
    ProductFormSet = inlineformset_factory(Product, Gallery, fields=('image',))
    if request.method == 'POST':
        form = ProductChangeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        product = Product.objects.get(slug=form.cleaned_data['slug'])
        formset = ProductFormSet(request.POST, request.FILES, instance=product)
        if formset.is_valid():
            formset.save()
        return redirect('controlpanel:products_index')
    else:
        form = ProductChangeForm()
        formset = ProductFormSet()
    template = 'cp/product_add.html'
    context = {'form': form, 'formset': formset}
    return render(request, template, context)


@staff_member_required
def order_add(request):
    OrderFormSet = inlineformset_factory(
        Order, OrderItem, fields=('product', 'price', 'quantity',))
    if request.method == 'POST':
        form = OrderChangeForm(request.POST)
        if form.is_valid():
            form.save()
        formset = OrderFormSet(request.POST)
        return redirect('controlpanel:orders_index')
    else:
        form = OrderChangeForm()
        formset = OrderFormSet()
    template = 'cp/order_add.html'
    context = {'form': form, 'formset': formset}
    return render(request, template, context)


@staff_member_required
def order_detail(request, id):
    '''
    открыли заказ order.client_exists = False
    ищем в базе клиентов клиента с таким же емейлом как в заказе
    если такой есть:
        выводим сообщение что такой клиент есть в базе и его емейл
        order.client_exists = True
        order.client = get_object_or_404(client)
        order.save()
    если такого нет:
        показываем галочку "сохранить клиента в базу"
            если ткнули(order.client_exists = True):
                создаем новый объект Клиент с данными из заказа
            если не ткнули(order.client_exists = False):
                ничего не делаем
    ???? привязывание к заказу клиента в какой момент делать ????
    '''
    alert = False
    errors = False
    order = get_object_or_404(Order, id=id)
    related_clients = Client.objects.filter(email=order.email)
    if related_clients.count == 0:
        order.client_exists == False
    order.read = True
    order.save()
    order_items = OrderItem.objects.filter(order=order)
    OrderFormSet = inlineformset_factory(
        Order, OrderItem, fields=('product', 'price', 'quantity',))
    if request.method == 'POST':
        form = OrderChangeForm(request.POST, instance=order)
        formset = OrderFormSet(request.POST, instance=order)
        if form.is_valid():
            form.save()
            alert = 'success'
        else:
            alert = 'danger'
            errors = form.errors
        if formset.is_valid():
            formset.save()
            alert = 'success'
        else:
            alert = 'danger'
            errors = formset.errors
        return redirect('controlpanel:orders_index')
    else:
        form = OrderChangeForm(initial={
            'phone': order.phone,
            'fullname': order.fullname,
            'email': order.email,
            'city': order.city,
            'street': order.street,
            'house_no': order.house_no,
            'flat_no': order.flat_no,
            'building_no': order.building_no,
            'postal_code': order.postal_code,
            'comment': order.comment,
            'call_me': order.call_me,
            'paid': order.paid,
            'client_exists': order.client_exists,
        })
        formset = OrderFormSet(instance=order)
    template = 'cp/order_detail.html'
    context = {'form': form, 'formset': formset, 'order': order,
               'order_items': order_items, 'alert': alert, 'errors': errors, 'related_clients':related_clients}
    return render(request, template, context)


@staff_member_required
def order_delete(request, id):
    order = get_object_or_404(Order, id=id)
    if request.method == 'POST':
        Order.objects.filter(id=id).delete()
        return redirect('controlpanel:orders_index')
    else:
        pass
    template = 'cp/order_delete.html'
    context = {'order': order}
    return render(request, template, context)
