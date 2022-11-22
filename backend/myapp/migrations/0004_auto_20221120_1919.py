# Generated by Django 3.2.16 on 2022-11-20 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_alignmentmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='alignmentmodel',
            name='json_file',
            field=models.FileField(default='image.jpg', upload_to='json/uploads/%Y/%m/%d'),
        ),
        migrations.AddField(
            model_name='alignmentmodel',
            name='video_file',
            field=models.FileField(default='image.jpg', upload_to='videos/uploads/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='alignmentmodel',
            name='audio_file',
            field=models.FileField(default='image.jpg', upload_to='audio/uploads/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='alignmentmodel',
            name='text_file',
            field=models.FileField(default='image.jpg', upload_to='images/uploads/%Y/%m/%d'),
        ),
    ]
