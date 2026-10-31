from django.contrib import admin
from .models import TaskModels

# Register your models here.
class AdminTask(admin.ModelAdmin):
    list_display= ['id','task_name', 'task_descp', 'task_added_at', 'task_status']
    list_filter = ['task_status']
    search_fields = ['task_name']
admin.site.register(TaskModels, AdminTask)
