from django.db import models

# Create your models here.

class React(models.Model):
    name=models.CharField(max_length=30)
    school=models.CharField(max_length=50)
    message=models.TextField()