# Generated by Django 3.2.16 on 2023-01-20 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20230120_0739'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userpersonalinfo',
            name='phone',
            field=models.CharField(max_length=40, unique=True),
        ),
        migrations.AlterField(
            model_name='userpersonalinfo',
            name='username',
            field=models.CharField(max_length=40, unique=True),
        ),
    ]
