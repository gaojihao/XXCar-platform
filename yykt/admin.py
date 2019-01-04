# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import *

# Register your models here.

admin.site.site_header = '星星课堂'
admin.site.site_title = '管理系统'
admin.site.index_title = '星星课堂'
admin.site.site_url = ''

admin.site.disable_action('delete_selected')

class CourseCategotyAdmin(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(CourseCategoty,CourseCategotyAdmin)

