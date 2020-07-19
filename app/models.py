from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Example(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    # name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    date = models.DateTimeField(blank=True, null=True)
    
    def __str__(self):
        return self.first_name

    def save(self, *args, **kwargs):
        self.first_name = self.user.first_name
        super(Example, self).save(*args, **kwargs)