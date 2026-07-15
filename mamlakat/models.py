from django.db import models

# Create your models here.
class Mamlakat(models.Model):
    name=models.CharField(max_length=100)
    plase=models.PositiveIntegerField()
    created_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)
    