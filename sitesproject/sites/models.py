from django.db import models

# Create your models here.

class Site(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return "{} Site".format(self.name)

class Item(models.Model):
    site = models.ForeignKey(Site, on_delete=models.CASCADE)
    date = models.DateField()
    a_value = models.DecimalField(default=0.0, decimal_places=2, max_digits=8)
    b_value = models.DecimalField(default=0.0, decimal_places=2, max_digits=8)
    def __str__(self):
        return str(self.date)