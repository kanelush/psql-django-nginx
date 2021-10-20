from django.db import models

# Create your models here.

class Test(models.Model):
    name = models.CharField(max_length=153)
    title = models.CharField(max_length=154)
    
    def __str__(self):
        return self.title
