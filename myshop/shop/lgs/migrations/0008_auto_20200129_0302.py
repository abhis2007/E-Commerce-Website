# Generated by Django 3.0.2 on 2020-01-28 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lgs', '0007_auto_20200124_1500'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactdb',
            name='CheckBox',
            field=models.IntegerField(),
        ),
    ]