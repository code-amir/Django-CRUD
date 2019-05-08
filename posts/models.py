from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class post(models.Model):
    user        =   models.CharField(max_length=50)
    title 		= 	models.CharField(max_length=50)
    description =   models.CharField(max_length=50)

    def __str__(self):
        return self.user.username
