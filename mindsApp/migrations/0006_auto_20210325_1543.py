# Generated by Django 3.1.7 on 2021-03-25 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mindsApp', '0005_auto_20210325_1423'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dynamicpage',
            name='image',
            field=models.ImageField(upload_to='dynamic/'),
        ),
        migrations.AlterField(
            model_name='dynamicpage',
            name='logo',
            field=models.ImageField(upload_to='dynamic/'),
        ),
    ]