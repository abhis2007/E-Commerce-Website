# Generated by Django 3.0.2 on 2020-02-04 22:27

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('lgs', '0026_orderupdate'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderupdate',
            name='dates',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
