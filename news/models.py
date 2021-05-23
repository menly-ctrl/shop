from django.db import models

class Item(models.Model):
    image = models.ImageField(upload_to="items/", verbose_name="Изображение")
    item_name = models.CharField(max_length=255)
    item_description = models.CharField(max_length=255)
    item_price = models.IntegerField()

