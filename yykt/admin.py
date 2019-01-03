# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.

admin.site.site_header = 'YYKT'
admin.site.site_title = '管理系统'
admin.site.index_title = ''
admin.site.site_url = ''

admin.site.disable_action('delete_selected')

