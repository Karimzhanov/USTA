from django.contrib import admin
from apps.ambassadorship.models import Ambassadorship, AmbassadorshipImage

# Register your models here.

@admin.register(Ambassadorship)
class AmbassadorshipAdmin(admin.ModelAdmin):
    list_display = ('title', 'description') 
    search_fields = ('title', 'description')  

@admin.register(AmbassadorshipImage)
class AmbassadorshipImageAdmin(admin.ModelAdmin):
    list_display = ('description', 'image') 
    search_fields = ('description',)  