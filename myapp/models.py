from django.db import models

# Create your models here.

class User(models.Model):
    ustudent = models.CharField(max_length = 20)
    utamil = models.CharField(max_length = 100)
    usocial = models.EmailField(max_length=254)
    umaths = models.CharField(max_length=15)
    uscience = models.CharField(max_length=15)
    uenglish = models.CharField(max_length=15)

    class Meta:
        db_table = "user"