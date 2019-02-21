from django.db import models
from django.contrib.auth.models import User
from datetime import date
from django.urls import reverse
# Create your models here.

class Employee(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    picture=models.CharField(max_length=40)
    department=models.CharField(max_length=50)
    role=models.CharField(max_length=50)
    email=models.EmailField(max_length=80)
    phone=models.CharField(max_length=15)

    def __str__(self):
        return f'{self.first_name}  {self.last_name}'

    def get_absolute_url(self):
        return reverse('employee_detail',args=[str(self.id)])


class Visitor(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    picture=models.CharField(max_length=40)
    phone=models.CharField(max_length=15)

    def __str__(self):
        return f'{self.first_name}  {self.last_name}'
    
    def get_absolute_url(self):
        return reverse('visitor_detail',args=[str(self.id)])
