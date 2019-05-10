from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class post(models.Model):
    user        =   models.ForeignKey(User,on_delete=models.CASCADE,related_name='posts')
    title 		= 	models.CharField(max_length=50)
    description =   models.TextField(max_length=100)

    def __str__(self):
        return self.user+self.title+self.description
