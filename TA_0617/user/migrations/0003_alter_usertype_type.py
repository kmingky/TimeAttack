# Generated by Django 4.0.5 on 2022-06-17 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0002_usertype_user_type"),
    ]

    operations = [
        migrations.AlterField(
            model_name="usertype",
            name="type",
            field=models.CharField(max_length=200, verbose_name="구분"),
        ),
    ]
