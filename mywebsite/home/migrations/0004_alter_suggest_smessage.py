# Generated by Django 4.0 on 2022-07-06 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_suggest'),
    ]

    operations = [
        migrations.AlterField(
            model_name='suggest',
            name='smessage',
            field=models.CharField(max_length=220),
        ),
    ]