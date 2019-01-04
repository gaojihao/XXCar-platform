# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class CourseCategoty(models.Model):
    name = models.CharField('类别', max_length=16, unique=True, error_messages={'unique':'这个分类已存在'})
    createTime = models.DateTimeField('创建时间',auto_now_add=True)
    updateTime = models.DateTimeField('更新时间', auto_now=True)
    

    def __str__(self):
        return self.name
    
    def __unicode__(self):
        return self.name
    
    def toDict(self):
        return {'name': self.name}
    
    class Meta:
        verbose_name_plural = '类别'
        verbose_name = '类别'