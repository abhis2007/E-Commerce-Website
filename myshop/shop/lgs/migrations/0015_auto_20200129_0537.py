# Generated by Django 3.0.2 on 2020-01-29 00:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lgs', '0014_auto_20200129_0534'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactdb',
            name='Address',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='contactdb',
            name='Comment',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='contactdb',
            name='Email',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='contactdb',
            name='Name',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='orderfromwebsite',
            name='city',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='orderfromwebsite',
            name='code',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='orderfromwebsite',
            name='email',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='orderfromwebsite',
            name='first_name',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='orderfromwebsite',
            name='goods_amount',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='orderfromwebsite',
            name='goods_count',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='orderfromwebsite',
            name='goods_name',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='orderfromwebsite',
            name='last_name',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='orderfromwebsite',
            name='local',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='orderfromwebsite',
            name='phone_number',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='orderfromwebsite',
            name='price',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='orderfromwebsite',
            name='state',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='product',
            name='Category',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='product',
            name='Description',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='product',
            name='SubCategory',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='product',
            name='productname',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='product',
            name='publish',
            field=models.DateField(max_length=500),
        ),
    ]
