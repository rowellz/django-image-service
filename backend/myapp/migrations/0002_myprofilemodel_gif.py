# Generated by Django 3.2.16 on 2022-10-26 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='myprofilemodel',
            name='gif',
            field=models.ImageField(default='image.jpg', upload_to='images/uploads/%Y/%m/%d'),
        ),
    ]
