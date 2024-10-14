from django.contrib import admin
from apps.collaboration.models import Сollaboration, Project, ProjectsPage, Award, MentoringPrograms

# Register your models here.

@admin.register(Сollaboration)
class СollaborationAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')  
    search_fields = ('title', 'description')  
    list_filter = ('title',) 

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')  
    search_fields = ('title', 'description')  
    list_filter = ('title',)  # 

@admin.register(ProjectsPage)
class ProjectsPageAdmin(admin.ModelAdmin):
    list_display = ('title',)  
    search_fields = ('title',) 
    filter_horizontal = ('projects',)  

@admin.register(Award)
class AwardAdmin(admin.ModelAdmin):
    list_display = ('title', 'description') 
    search_fields = ('title', 'description')  
    list_filter = ('title',)  

@admin.register(MentoringPrograms)
class MentoringProgramsAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'additional_text')  
    search_fields = ('title', 'description')  
    list_filter = ('title',)  
