from django.db import models

# Create your models here.
class blog(models.Model):
    name = models.CharField(max_length=100)
    day = models.IntegerField()
    month = models.CharField(max_length=50)
    img = models.ImageField(upload_to='picture')
    desc = models.TextField()
