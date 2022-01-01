from django.db import models
from category.models import Category

# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='photos/products', blank=True)
    image_hover = models.ImageField(upload_to='photos/products', blank=True)
    tag_class = models.CharField(max_length=15, blank=True)
    tag = models.CharField(max_length=10, blank=True)

    def __str__(self):
        return self.product_name

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

    @property
    def image_hoverURL(self):
        try:
            url = self.image_hover.url
        except:
            url = ''
        return url




class MediumBanner(models.Model):
    m_headline = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    m_image = models.ImageField(upload_to='photos/medium_banners', blank=True)
    m_tag = models.CharField(max_length=30, blank=False)
    m_btn_text = models.CharField(max_length=15, blank=False)


    def __str__(self):
        return self.m_headline

    @property
    def m_imageURL(self):
        try:
            url = self.m_image.url
        except:
            url = ''
        return url
