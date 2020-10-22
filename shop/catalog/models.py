from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    number = models.IntegerField(default=0, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)
    image = models.ImageField(upload_to='categoryimages/', blank=True, null = True)

    def get_absolute_url(self):
        return reverse('catalog:product_list_by_category', args=[self.slug])

    class Meta:
        ordering = ('number',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name
    
    def get_products_len(self):
        products = Product.objects.filter(available=True)
        products = products.filter(category=self)
        return len(products)


class Product(models.Model):
    category = models.ForeignKey(
        Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)
    mainimage = models.ImageField(upload_to='gallery', blank=True)
    description = models.TextField(blank=True)
    code = models.TextField(blank=True)
    size = models.TextField(blank=True)
    contents = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=0)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('catalog:product_detail',
                       args=[self.id, self.slug])

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name


class Gallery(models.Model):
    image = models.ImageField(upload_to='gallery')
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='images')

    def get_img_url(self):
        return self.image.url
