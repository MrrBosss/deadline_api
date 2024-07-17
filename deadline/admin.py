from django.contrib import admin
from .models import Project, Process, Domain, Developer

# Register your models here.



admin.site.register(Process)

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('project_name', 'start_day', 'end_day')
    search_fields = ('project_name', 'developer_name')
    list_filter = ('start_day', 'end_day')

admin.site.register(Domain)

@admin.register(Developer)
class DeveloperAdmin(admin.ModelAdmin):
    list_display = ('developer_name',)
    search_fields = ('developer_name',)