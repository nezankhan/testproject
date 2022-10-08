from django.db import models
from django.utils import timezone
# Create your models here.


class Inventory(models.Model):
    item_id = models.IntegerField(primary_key=True,serialize=True)
    image = models.ImageField(default='default.jpg',upload_to='inventory_pics')
    product_name = models.CharField(max_length=100)
    description = models.TextField() #unrestricted text
    #date_posted = models.DateTimeField(auto_now_add=True) auto_now adds date when it was created but you cant change it later
    date_created = models.DateTimeField(default=timezone.now)
    product_type = models.TextField()
    stock_level = models.IntegerField()

    def __str__(self):
        return self.product_name

class SaleOrders(models.Model):
    order_number = models.IntegerField(primary_key=True,serialize=True)
    item_id = models.ForeignKey(Inventory, on_delete=models.CASCADE)
    quantity= models.IntegerField()