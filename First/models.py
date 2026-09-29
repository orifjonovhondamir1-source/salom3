from django.db import models

# Create your models here.
class TTM(models.Model):
    img1 = models.ImageField(upload_to='media', null=True)
    ismi = models.CharField(max_length=1000 , null=True)
    yoshi = models.CharField(max_length=1000 ,null=True)
    ishi = models.CharField(max_length=1000, null=True)    
    is_arzon = models.BooleanField(default=False)
    def __str__(self):
        return self.ismi
    
class  Uzbek(models.Model):
    img = models.ImageField(upload_to='media', null=True)
    narxi= models.IntegerField(max_length=1000 , null=True)
    sikidka = models.IntegerField(max_length=1000 ,null=True)
    izoh = models.CharField(max_length=1000, null=True)    
    is_arzon = models.BooleanField(default=False)
    is_bozor = models.BooleanField(default=False)
    is_sotulda = models.BooleanField(default=False)
    is_sotildi = models.BooleanField(default=False)

    def __str__(self):
        return self.izoh
    
    
import uuid  
from django.db import models

class Mahsulot(models.Model):
  
    nomi = models.CharField(max_length=255)
    narxi = models.IntegerField()  
    narx_decimal = models.DecimalField(max_digits=10, decimal_places=2)
    soni = models.PositiveIntegerField()
    manfiy_bolmagan = models.PositiveBigIntegerField()
    reyting = models.FloatField()
    izoh = models.TextField()

    
    rasm = models.ImageField(upload_to='media/')  
    fayl = models.FileField(upload_to='files/')
    
    
    email = models.EmailField()
    sayt = models.URLField()
    telefon = models.CharField(max_length=20)
    slug = models.SlugField(max_length=20)
    ip_manzil = models.GenericIPAddressField()

    tugilgan_sana = models.DateField()
    yaratilgan_vaqt = models.DateTimeField(auto_now_add=True)
    yangilangan_vaqt = models.DateTimeField(auto_now=True)
    aktiv = models.BooleanField(default=True)
    
    uuid =  models.UUIDField(default=True, editable=False, unique=True)
    json_data = models.JSONField(null=True, blank=True)


    def __str__(self):
        return self.nomi
    
class Salom(models.Model):
    logo = models.ImageField(upload_to='media', null=True)
    name = models.CharField(max_length=1000 , null=True)
    mean = models.CharField(max_length=1000 ,null=True)
    div = models.BooleanField(default=False)


    def __str__(self):
        return self.name
    