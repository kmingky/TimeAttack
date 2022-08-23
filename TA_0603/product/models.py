from django.db import models

# Create your models here.


class Category(models.Model):
    class Meta:
        db_table = "starbucks_category"

    def __str__(self):
        return self.drink_category

    drink_category = models.CharField(max_length=256, null=False, verbose_name="음료구분")


class Drink(models.Model):
    class Meta:
        db_table = "starbucks_drink"

    def __str__(self):
        return self.drink_name

    drink_name = models.CharField(max_length=256, null=False, verbose_name="음료이름")
    drink_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    drink_info = models.CharField(max_length=256, null=False, verbose_name="영양정보")
    drink_allergy = models.CharField(max_length=256, null=False, verbose_name="알러지")
