from django.db import models

# Create your models here.
class UserClass(models.Model):
    class Meta:
        db_table = "my_user"

    email = models.EmailField(max_length=128, null=False)
    password = models.CharField(max_length=256, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
