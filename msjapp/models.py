from django.db import models

# Create your models here.
class FormData(models.Model):
    name=models.CharField(max_length=20)
    mobile=models.CharField(max_length=10)
    email=models.EmailField(max_length=200)
    msg=models.CharField(max_length=300)

