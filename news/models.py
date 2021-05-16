from django.db import models

class Items(models.Model):
    image = models.ImageField(upload_to="items/")
    item_name = models.CharField(max_length=255)
    item_description = models.CharField(max_length=255)
    item_price = models.IntegerField()

