from django.conf.urls import url
from . import views

app_name = 'cart'

urlpatterns = [
    url(r'^$', views.cart_detail, name='cart_detail'),
    url(r'^add/(?P<product_id>\d+)/$', views.cart_add, name='cart_add'),
    url(r'^remove/(?P<product_id>\d+)/$', views.cart_remove, name='cart_remove'),
    url(r'^add_quantity/(?P<product_id>\d+)/$', views.cart_add_quantity, name='cart_add_quantity'),
    url(r'^decrease_quantity/(?P<product_id>\d+)/$',
        views.cart_decrease_quantity, name='cart_decrease_quantity'),
]
