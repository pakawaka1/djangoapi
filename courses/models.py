from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=200)
    language = models.CharField(max_length=100)
    price = models.CharField(max_length=10)
    level = models.CharField(max_length=10, default='level')
    prereqs = models.CharField(max_length=200, default='prereqs')

    def  __str__(self):
        return self.name
