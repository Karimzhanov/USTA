from django.contrib import admin
from apps.about_the_community.models import About, CommunityImage

# Register your models here.
@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')  
    search_fields = ('title', 'description')  
    list_filter = ('title',)  

@admin.register(CommunityImage)
class CommunityImageAdmin(admin.ModelAdmin):
    list_display = ('image', 'description') 
    search_fields = ('description',)
    list_filter = ('description',)  
