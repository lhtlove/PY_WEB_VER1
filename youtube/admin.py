from django.contrib import admin
from youtube.models import Youtube

# Register your models here.
class YoutubeAdmin(admin.ModelAdmin) :
    list_display = ('title', 'url')


admin.site.register(Youtube, YoutubeAdmin)
