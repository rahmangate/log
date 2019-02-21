from django.contrib import admin

# Register your models here.
from logapp.models import Employee,Visitor

admin.site.register(Employee)
admin.site.register(Visitor)