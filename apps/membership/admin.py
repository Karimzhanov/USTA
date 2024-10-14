from django.contrib import admin
from apps.membership.models import Membership, ContentBlock, Category, StepInstruction

# Register your models here.

@admin.register(Membership)
class MembershipAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')  
    search_fields = ('title', 'description') 

@admin.register(ContentBlock)
class ContentBlockAdmin(admin.ModelAdmin):
    list_display = ('title', 'category')  
    search_fields = ('title', 'description')  

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)  
    search_fields = ('title',)  

@admin.register(StepInstruction)
class StepInstructionAdmin(admin.ModelAdmin):
    list_display = ('step_number', 'title')  
    search_fields = ('title',)  
    ordering = ('step_number',)  

