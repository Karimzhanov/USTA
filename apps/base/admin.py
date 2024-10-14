from django.contrib import admin
from apps.base.models import PageContent, ContentBlock,Partner, Event, EventImage, ProjectParticipation, ProjectImage, TeamMember, ContentBlocks

# Register your models here.

@admin.register(PageContent)
class PageContentAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')  
    search_fields = ('title', 'description')  
    list_filter = ('title',)  


@admin.register(ContentBlock)
class ContentBlockAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'date')
    search_fields = ('title', 'description')  
    list_filter = ('date',)  

@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ('name',)  
    search_fields = ('name',)  

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')  
    search_fields = ('title', 'description')  

@admin.register(EventImage)
class EventImageAdmin(admin.ModelAdmin):
    list_display = ('event', 'image')  
    search_fields = ('event__title',) 

@admin.register(ProjectParticipation)
class ProjectParticipationAdmin(admin.ModelAdmin):
    list_display = ('title', 'description') 
    search_fields = ('title', 'description')  

@admin.register(ProjectImage)
class ProjectImageAdmin(admin.ModelAdmin):
    list_display = ('project', 'image')  
    search_fields = ('project__title',)  

@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'position') 
    search_fields = ('full_name', 'position')  

@admin.register(ContentBlocks)
class ContentBlocksAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'description')  
    search_fields = ('title', 'description') 
    list_filter = ('category',) 
