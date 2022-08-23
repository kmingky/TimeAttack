# Generated by Django 4.0.5 on 2022-06-03 07:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "drink_category",
                    models.CharField(max_length=256, verbose_name="음료구분"),
                ),
            ],
            options={"db_table": "starbucks_category",},
        ),
        migrations.CreateModel(
            name="Drink",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("drink_name", models.CharField(max_length=256, verbose_name="음료이름")),
                ("drink_info", models.CharField(max_length=256, verbose_name="영양정보")),
                ("drink_allergy", models.CharField(max_length=256, verbose_name="알러지")),
                (
                    "drink_category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="product.category",
                    ),
                ),
            ],
            options={"db_table": "starbucks_drink",},
        ),
    ]