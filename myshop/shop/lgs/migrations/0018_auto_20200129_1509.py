# Generated by Django 3.0.2 on 2020-01-29 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lgs', '0017_auto_20200129_1508'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderfromwebsite',
            name='goods_count',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='orderfromwebsite',
            name='goods_name',
            field=models.CharField(max_length=50),
        ),
    ]
