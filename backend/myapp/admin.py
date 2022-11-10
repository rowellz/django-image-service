
from django.contrib import admin
from .models import MyProfileModel
# Register your models here.


class MyProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'image', 'gif')
    list_display_links = ('name', 'image', 'gif')
    search_fields = ('name', 'image', 'gif')
    list_per_page = 25
    list_filter = ('name',)


admin.site.register(MyProfileModel, MyProfileAdmin)
