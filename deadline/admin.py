from django.contrib import admin

from .models import Project, Status, Job
# Register your models here.

admin.site.register(Job)

admin.site.register(Status)

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name','user','start_day', 'end_day','is_finish')
    search_fields = ('name',)
    list_filter = ('start_day','end_day') 
