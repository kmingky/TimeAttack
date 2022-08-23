from django.db import models


# Create your models here.


class User(models.Model):
    class Meta:
        db_table = "USER"

    def __str__(self):
        return self.username

    username = models.CharField(max_length=256, null=False, verbose_name="ID")
    password = models.CharField(max_length=256, null=False, verbose_name="PASSWORD")
