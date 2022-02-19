from django.db import models
from django.urls import reverse

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=70)
    subject = models.CharField(max_length=200)
    email_address = models.EmailField()
    message = models.TextField()
    
    def __str__(self):
        return self.email_address
    
class Password(models.Model):
    length = models.CharField(max_length=70)
    def __str__(self):
        return self.length