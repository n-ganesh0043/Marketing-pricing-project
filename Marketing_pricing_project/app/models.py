from django.db import models

# Create your models here.

class ProductTAble(models.Model):
    prd_id=models.IntegerField(primary_key=True)
    prd_name=models.CharField(max_length=30)
    prd_quntity=models.CharField(max_length=20)
    prd_price=models.IntegerField(default=False)
    prd_manf_dt=models.DateField()
    prd_exp_dt=models.DateField()
