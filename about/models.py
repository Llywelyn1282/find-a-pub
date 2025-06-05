from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class About(models.Model):
    title = models.CharField(max_length=200)
    updated_on = models.DateTimeField(auto_now=True)
    description = models.TextField()

    def __str__(self):
        return self.title


class ContactForm(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()
    read = models.BooleanField(default=False)

    def __str__(self):
        return f"Message from {self.name}"
