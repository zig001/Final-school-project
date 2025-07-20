from django.db import models

# Create your models here.

class Images(models.Model):
    id = models.IntegerField(primary_key=True)
    desc = models.CharField(max_length=128, default='.')
    image = models.ImageField(upload_to='customImages')


class Classmates(models.Model):
    id = models.IntegerField(primary_key=True)
    first_name = models.CharField(null=False, max_length=128)
    last_name = models.CharField(null=False, max_length=128)
    description = models.CharField(max_length=256)
    profile_image = models.ForeignKey(Images, on_delete=models.CASCADE)
