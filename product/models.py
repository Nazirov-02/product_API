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


class Product(BaseModel):
    name = models.CharField(max_length=100,unique=True)
    slug = models.SlugField(max_length=100,unique=True,null=True,blank=True)
    description = models.TextField()
    price = models.IntegerField()
    discount = models.PositiveIntegerField()
    image = models.ImageField()
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return self.name

    def discount_price(self):
        if self.discount > 0:
            self.price = self.price * Decimal((1 - self.discount / 100))
        return self.price.quantize(Decimal('0.01'))

    def img_url(self):
        if self.image:
            return self.image.url
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)