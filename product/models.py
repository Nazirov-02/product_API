from django.db import models
from decimal import Decimal
from django.utils import timezone
from django.utils.text import slugify

# Create your models here.

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True


class Category(BaseModel):
    title = models.CharField(max_length=100,unique=True)
    slug = models.SlugField(max_length=100,null=True,blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class Product(BaseModel):
    name = models.CharField(max_length=100,unique=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name='products',null=True,blank=True)
    slug = models.SlugField(max_length=100,unique=True,null=True,blank=True)
    description = models.TextField()
    price = models.IntegerField()
    discount = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return self.name

    def discount_price(self):
        if self.discount > 0:
            self.price = self.price * Decimal((1 - self.discount / 100))
        return self.price.quantize(Decimal('0.01'))

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

class Comment(BaseModel):
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name='comments',null=True,blank=True)
    comment = models.TextField()

class Image(BaseModel):
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name='images')
    image = models.ImageField()
    is_main = models.BooleanField(null=True,blank=True)

    def __str__(self):
        return self.product.name

    def absolute_url(self):
        return self.image.url