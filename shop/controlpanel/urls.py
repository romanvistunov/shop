from django.urls import path
from . import views

app_name = 'controlpanel'

urlpatterns = [
    path('', views.panel_index, name='panel_index'),
    path('categories/', views.category_index, name='category_index'),
    path('products/', views.products_index, name='products_index'),
    path('orders/', views.orders_index, name='orders_index'),
    path('clients/', views.clients_index, name='clients_index'),
    path('categories/detail/<int:id>/',
         views.category_detail, name='category_detail'),
    path('products/detail/<int:id>/',
         views.product_detail, name='product_detail'),
    path('orders/detail/<int:id>/',
         views.order_detail, name='order_detail'),
    path('categories/delete/<int:id>/',
         views.category_delete, name='category_delete'),
    path('products/delete/<int:id>/',
         views.product_delete, name='product_delete'),
    path('orders/delete/<int:id>/',
         views.order_delete, name='order_delete'),
    path('categories/add/',
         views.category_add, name='category_add'),
    path('products/add/',
         views.product_add, name='product_add'),
    path('orders/add/',
         views.order_add, name='order_add'),
     
]
