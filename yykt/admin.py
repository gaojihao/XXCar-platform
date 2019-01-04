# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import *

admin.site.site_header = 'xx课堂'
admin.site.site_title = 'zz系统'
admin.site.index_title = 'yy课堂'
admin.site.site_url = ''

admin.site.disable_action('delete_selected')

class CourseCategotyAdmin(admin.ModelAdmin):
    list_display = ['name']

class TagAdmin(admin.ModelAdmin):
    list_display = ['tag']


admin.site.register(CourseCategoty,CourseCategotyAdmin)
admin.site.register(Tag,TagAdmin)

