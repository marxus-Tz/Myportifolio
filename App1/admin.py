from django.contrib import admin
from .models import projects,ContactMessage


# Register your models here.
admin.site.register(projects)
class projectAdmin(admin.ModelAdmin):
    list_display=['title', 'description', 'url']
    list_filter=['title',]
    search_fields=['title','url']
    list_per_page = 10
    # list_editable=['title']
    
admin.site.register(ContactMessage)
