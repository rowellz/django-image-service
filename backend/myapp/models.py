from django.db import models

# Create your models here.


class MyProfileModel(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(
        upload_to='images/uploads/%Y/%m/%d', default='image.jpg')
    gif = models.ImageField(
        upload_to='images/uploads/%Y/%m/%d', default='image.jpg')

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "My Profile"
        verbose_name_plural = "My Profiles"
        db_table = "my_profile"

class AlignmentModel(models.Model):
    name = models.CharField(max_length=50, default="frown")
    text_file = models.FileField(
        upload_to='images/uploads/%Y/%m/%d')
    audio_file = models.FileField(
        upload_to='images/uploads/%Y/%m/%d')

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name_plural = "force_alignments"
        db_table = "force_alignment"