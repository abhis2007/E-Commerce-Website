from django.db import models

# Create your models here.
class product(models.Model):
    ProductId=models.AutoField
    productname=models.CharField(max_length=500)
    Image=models.ImageField(upload_to="lgs/images",default="")
    Price = models.IntegerField(default=0)
    Description=models.CharField(max_length=500)
    publish=models.DateField(max_length=500)
    Category=models.CharField(max_length=500)
    SubCategory = models.CharField(max_length=500)
    def __str__(self):
        return self.productname

class contactdb(models.Model):
    Name=models.CharField(max_length=500)
    Phone=models.IntegerField()
    Email=models.CharField(max_length=500)
    Address=models.CharField(max_length=500)
    CheckBox=models.IntegerField()
    Comment=models.CharField(max_length=500)

    def __str__(self):
        return self.Name

class orderfromwebsite(models.Model):
    goods_count=models.CharField(max_length=500,null=True)
    goods_name=models.CharField(max_length=500,null=True)
    goods_amount=models.CharField(max_length=500,null=True)
    price= models.CharField(max_length=500)
    first_name = models.CharField(max_length=500)
    last_name =  models.CharField(max_length=500)
    phone_number =models.CharField(max_length=500)
    email = models.CharField(max_length=500)
    state =  models.CharField(max_length=500)
    city = models.CharField(max_length=500)
    code =  models.CharField(max_length=500)
    local = models.CharField(max_length=500)
    orderId = models.CharField(max_length=500,primary_key=True)

    def _str_(self):
        return self.orderId


class after_payment(models.Model):
    orderid=models.CharField(max_length=500,primary_key=True)
    transaction_amount=models.FloatField()
    transaction_date=models.CharField(max_length=500,default="notfound")
    currency=models.CharField(max_length=500)
    status=models.CharField(max_length=500)
    response_code=models.CharField(max_length=500)
    response_message=models.CharField(max_length=500)
    bank_transaction_id=models.CharField(max_length=500,default="NOT GENERATED")
    transaction_id=models.CharField(max_length=500)
    checksum=models.CharField(max_length=500,default='checksum not gone for verification')

    def __str__(self):
        return self.orderid


