from django.contrib import admin
from apps.educert.models import Educert, Contentblock, Videoo

# Register your models here.

@admin.register(Educert)
class EducertAdmin(admin.ModelAdmin):
    list_display = ('title', 'description') 
    search_fields = ('title', 'description') 

@admin.register(Contentblock)
class ContentblockAdmin(admin.ModelAdmin):
    list_display = ('title', 'category') 
    search_fields = ('title', 'description')  

@admin.register(Videoo)
class VideooAdmin(admin.ModelAdmin):
    list_display = ('title', 'video_url')  
    search_fields = ('title', 'description')  
