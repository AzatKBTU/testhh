from django.db import models


class Restaurant(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=250)
    address = models.CharField(max_length=250)

    def __str__(self):
        return self.title

class Menu(models.Model):
    company = models.ForeignKey(Restaurant, on_delete = models.CASCADE)
    name = models.CharField(max_length=30)
    cheese_type = models.CharField(max_length=250)
    dough_thickness = models.PositiveIntegerField()
    secret_ing = models.CharField(max_length=250)

    def __str__(self):
        return self.name
