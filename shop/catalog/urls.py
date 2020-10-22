from django.urls import path
from django.conf.urls import url
from catalog import views

app_name = 'catalog'

urlpatterns = [
    #path("", views.catalog_all, name="catalog_all"),
    url(r'^(?P<category_slug>[-\w]+)/$',
        views.product_list, name='product_list_by_category'),
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$',
        views.product_detail, name='product_detail')
]
