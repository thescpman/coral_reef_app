from django.db import models

# Create your models here.

class Review(models.Model):
    name = models.TextField(max_length=500)
    date_added = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        """Return string"""
        return self.name
