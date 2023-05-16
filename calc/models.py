from django.db import models
 
# Create your models here.
class food(models.Model):
    name= models.CharField(max_length=100)
    desc= models.TextField()
    image= models.ImageField(upload_to='food_images')
    price= models.IntegerField()
    type = models.TextField()
    d_price = models.IntegerField(default=0)
    active = models.BooleanField(default=True)
class order(models.Model):
    username = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    province = models.CharField(max_length=100)
    ward = models.CharField(max_length=100)
    commune = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    time = models.DateTimeField(auto_now_add=True)
    total_price = models.IntegerField()
    CK = models.BooleanField(default=True)
    status = models.CharField(max_length=100)
class OrderLine(models.Model):
    orderid = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    food = models.CharField(max_length=100)
    name= models.CharField(max_length=100)
    price= models.IntegerField()
    quantity = models.IntegerField(null= True)
    image= models.ImageField(upload_to='food_images')
    status = models.BooleanField(default=False)
class CanvasImage(models.Model):
    username = models.CharField(max_length=100)
    image = models.ImageField(upload_to='canvas_images')
