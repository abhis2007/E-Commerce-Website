# Generated by Django 3.0.1 on 2019-12-26 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lgs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='publish',
            field=models.DateField(max_length=50),
        ),
    ]