from django.db import models

# Create your models here.
class Food(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField(max_length=255)
    image = models.ImageField()
    price= models.PositiveIntegerField()

    def __str__(self):
        return self.name
   
    class Meta:
        verbose_name_plural = "Food"