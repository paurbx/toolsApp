# Generated by Django 3.1.5 on 2021-11-22 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0005_auto_20211122_1821'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='header',
            field=models.CharField(max_length=25),
        ),
    ]