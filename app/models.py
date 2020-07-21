from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Player(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.first_name

    def save(self, *args, **kwargs):
        self.first_name = self.user.first_name
        super(Player, self).save(*args, **kwargs)

class Course(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Birdie(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    # hole technically makes more sense in Course, but shenanigans...
    string_choices = tuple((str(x), str(x)) for x in range(1,19))
    hole = models.CharField(max_length=2, null=True, blank=True, choices = string_choices, default='1')
    date = models.DateTimeField(blank=True, null=True)
