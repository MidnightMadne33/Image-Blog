# Generated by Django 2.1.7 on 2019-02-26 02:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserPage', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=50)),
                ('TextContent', models.TextField()),
                ('Date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='Bio',
            field=models.TextField(max_length=100),
        ),
    ]
