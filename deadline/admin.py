from django.contrib import admin
from .models import Department, Project, Task, Job

# Register your models here.

admin.site.register(Job)

admin.site.register(Department)

admin.site.register(Task)

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_day', 'end_day')
    search_fields = ('name',)
    list_filter = ('start_day', 'end_day')
