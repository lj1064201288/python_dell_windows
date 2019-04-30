from django.contrib import admin
from .models import *
import time
# Register your models here.


admin.site.site_header = '欢迎来到Django课堂'
admin.site.site_title = '这是标题'
admin.site.index_title = '这是首页标语'

class AdminClassRoom(admin.ModelAdmin):
    pass

class AdminTeacher(admin.ModelAdmin):
    list_per_page = 2
    actions_on_bottom = True
    actions_on_top = False
    list_display = ['name', 'room', 'curTime', 'getRoom']
    search_fields = ['name']
   # fields = ['name', 'course']

    fieldsets = (
        ('基本信息', {'fields':['name',]}),
        ('其他信息', {'fields':['course', 'room']}),
    )

class AdminStudent(admin.ModelAdmin):
    pass


admin.site.register(ClassRoom, AdminClassRoom)
admin.site.register(Teacher, AdminTeacher)
admin.site.register(Student, AdminStudent)