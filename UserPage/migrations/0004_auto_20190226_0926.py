# Generated by Django 2.1.7 on 2019-02-26 09:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('UserPage', '0003_auto_20190226_0847'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Blog',
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
