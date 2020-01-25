from django.db import models

# Create your models here.
class product(models.Model):
    ProductId=models.AutoField
    productname=models.CharField(max_length=50)
    Image=models.ImageField(upload_to="lgs/images",default="")
    Price = models.IntegerField(default=0)
    Description=models.CharField(max_length=350)
    publish=models.DateField(max_length=50)
    Category=models.CharField(max_length=50)
    SubCategory = models.CharField(max_length=50)
    def __str__(self):
        return self.productname

class contactdb(models.Model):
    Name=models.CharField(max_length=50)
    Phone=models.IntegerField()
    Email=models.CharField(max_length=50)
    Address=models.CharField(max_length=50)
    CheckBox=models.IntegerField(max_length=5)
    Comment=models.CharField(max_length=50)

    def __str__(self):
        return self.Name

class orderfromwebsite(models.Model):
    price= models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name =  models.CharField(max_length=50)
    phone_number =models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    state =  models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    code =  models.CharField(max_length=50)
    local = models.CharField(max_length=50)
    orderId = models.AutoField(primary_key=True)

    def _str_(self):
        return self.email
