import abc
from django.db import models

class Profile(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    about = models.CharField(max_length=500)
    date_added = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['-date_added']
