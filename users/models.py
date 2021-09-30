from django.db import models




class User(models.Model):
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    email = models.EmailField()


    def __str__(self):
        return self.first_name

