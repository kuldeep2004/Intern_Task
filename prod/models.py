from django.db import models

# Create your models here.
class Product(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)
    price = models.IntegerField()
    discountPercentage = models.DecimalField(decimal_places=2, max_digits=10000)
    rating = models.DecimalField(decimal_places=2, max_digits=10000, default=0.0)
    numberOfPeopleRated = models.IntegerField(default=0)
    stock = models.IntegerField()
    brand = models.CharField(max_length=120)
    category = models.CharField(max_length=120)
    thumbnail = models.URLField(blank=True, null=True)
    images = models.ManyToManyField('Image', related_name='products', blank=True)

    def __str__(self):
        return self.title
    
class Image(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_images')
    image = models.URLField()

    def __str__(self):
        return self.product.title if self.product else 'No associated product'
