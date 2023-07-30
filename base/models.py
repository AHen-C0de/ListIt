from django.db import models

class List(models.Model):
    name = models.CharField(max_length=30, unique=True)

    def __str__(self):
      return self.name


class Item(models.Model):
    name = models.CharField(max_length=30, unique=True)
    list = models.ForeignKey(
        List,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name
