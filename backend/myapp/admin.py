
from django.contrib import admin
from .models import MyProfileModel, AlignmentModel
# Register your models here.


class MyProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'image', 'gif')
    list_display_links = ('name', 'image', 'gif')
    search_fields = ('name', 'image', 'gif')
    list_per_page = 25
    list_filter = ('name',)

class AlignmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'text_file', 'audio_file', 'transcription_json', 'video_file')
    list_display_links = ('name', 'text_file', 'audio_file', 'transcription_json', 'video_file')
    search_fields = ('name', 'text_file', 'audio_file', 'transcription_json', 'video_file')
    list_per_page = 25
    list_filter = ('name',)


admin.site.register(MyProfileModel, MyProfileAdmin)
admin.site.register(AlignmentModel, AlignmentAdmin)
