# Generated by Django 3.0.1 on 2020-01-21 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lgs', '0003_auto_20191227_0133'),
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('Phone', models.IntegerField(max_length=13)),
                ('Email', models.CharField(max_length=50)),
                ('Address', models.CharField(max_length=50)),
                ('CheckBox', models.IntegerField(max_length=5)),
                ('Comment', models.CharField(max_length=50)),
            ],
        ),
    ]