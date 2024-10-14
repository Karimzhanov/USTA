from django.contrib import admin
from apps.events.models import Events, Eventss, Announcement, AnnualEvent, VideoContent, VideoContents

# Register your models here.

@admin.register(Events)
class EventsAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')  
    search_fields = ('title', 'description') 

@admin.register(Eventss)
class EventssAdmin(admin.ModelAdmin):
    list_display = ('title', 'date')  
    search_fields = ('title',) 

@admin.register(Announcement)
class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')  
    search_fields = ('title', 'description') 

@admin.register(AnnualEvent)
class AnnualEventAdmin(admin.ModelAdmin):
    list_display = ('title',)  
    search_fields = ('title',) 

@admin.register(VideoContent)
class VideoContentAdmin(admin.ModelAdmin):
    list_display = ('title', 'video_url')  
    search_fields = ('title', 'description') 

@admin.register(VideoContents)
class VideoContentsAdmin(admin.ModelAdmin):
    list_display = ('title', 'video_url')  
    search_fields = ('title', 'description') 
