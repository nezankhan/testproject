from pickle import FALSE
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
    quantity= models.IntegerField(null =False)
    shipped_date = models.DateField(null = False)

    def __str__(self):
        return self.order_number

class Employees(models.Model):
    EMP_ID = models.IntegerField(primary_key=True,serialize=True)
    First_Name = models.CharField(max_length=100)
    Last_Name = models.CharField(max_length=100)
    Title = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    hired_date = models.DateField(null = False)

    def __str__(self):
        full_name = self.First_Name + " " + self.Last_Name
        return full_name

class PurchaseOrders(models.Model):
    PO_ID = models.IntegerField(primary_key=True,serialize=True)
    item_id = models.ForeignKey(Inventory, on_delete=models.CASCADE)
    quantity = models.IntegerField(null =False)
    Purchase_date = models.DateField(null = False)

    def __str__(self):
        return self.PO_ID

class Customers(models.Model):
    customer_id = models.IntegerField(primary_key=True,serialize=True)
    First_Name = models.CharField(max_length=100)
    Last_Name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    city = models.CharField(max_length=100)

    def __str__(self):
        full_name = self.First_Name + " " + self.Last_Name
        return full_name

class SaleInvoices(models.Model):
    invoice_number = models.IntegerField(primary_key=True,serialize=True)
    Order_Number = models.ForeignKey(SaleOrders, on_delete=models.CASCADE)
    Customer_ID = models.ForeignKey(Customers, on_delete=models.CASCADE)
    EMP_ID = models.ForeignKey(Employees, on_delete=models.CASCADE)
    DISCOUNT = models.FloatField()
    Invoice_Date = models.DateField(null = False)
     
    def __str__(self):
        return self.invoice_number

class Suppliers(models.Model):
    supplier_id = models.IntegerField(primary_key=True,serialize=True)
    supplier_address = models.CharField(max_length=100)
    Company_Name = models.CharField(max_length=100, null= False)
    Net_TERMS = models.IntegerField()
    Date_Contracted = models.DateField(null = False)

    def __str__(self):
        return self.Company_Name

class PurchaseInvoices(models.Model):
    Purchase_number = models.IntegerField(primary_key=True,serialize=True)
    PO_ID = models.ForeignKey(PurchaseOrders, on_delete=models.CASCADE)
    Supplier_ID = models.ForeignKey(Suppliers, on_delete=models.CASCADE)
    Amount  = models.FloatField()
    Purchase_Date = models.DateField(null = False)


    def __str__(self):
        return self.Purchase_number

