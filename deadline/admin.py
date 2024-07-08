from django.contrib import admin
from .models import Project, Process

# Register your models here.



admin.site.register(Process)

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('project_name', 'developer_name', 'start_day', 'end_day')
    search_fields = ('project_name', 'developer_name')
    list_filter = ('start_day', 'end_day')

# @admin.register(AdditionalInfo)
# class AdditionalInfoAdmin(admin.ModelAdmin):
#     list_display = ('id', 'short_definition')
#     search_fields = ('definition',)

#     def short_definition(self, obj):
#         return obj.definition[:50] if obj.definition else 'No definition'
#     short_definition.short_description = 'Definition'
