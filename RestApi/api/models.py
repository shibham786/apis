from django.db import models
import uuid
from django.contrib.auth.models import User

# Create your models here.
class Department(models.Model):
    dname = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)

    def __str__(self):
        return self.dname

class ImageTest(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(default="default.jpg",null=True,blank=True)
    id = models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)

    def __str__(self):
        return self.title

class Employee(models.Model):
    ename = models.CharField(max_length=200,null=True,blank=True)
    esal = models.IntegerField(null=True,blank=True)
    dept = models.ForeignKey(Department,null=True,blank=True,on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)

    def __str__(self):
        return self.ename





