# Generated by Django 3.0.2 on 2020-01-29 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lgs', '0021_auto_20200129_1808'),
    ]

    operations = [
        migrations.AlterField(
            model_name='after_payment',
            name='transaction_date',
            field=models.CharField(default='notfound', max_length=500),
        ),
    ]