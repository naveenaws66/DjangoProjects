from django.db import models

class people(models.Model):
    name = models.CharField(max_length=200)
    phone = models.IntegerField(default=0)
    def __str__(self):
        return self.name
