# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

COURSE_FORMAT_CHOICES = (
    (0, u'视频'),
    (1, u'音频'),
    (3, u'文章'),
)


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

class Tag(models.Model):
    tag = models.CharField('标签', max_length=16, unique=True, error_messages={'unique':'这个标签已存在'})
    createTime = models.DateTimeField('创建时间',auto_now_add=True)
    updateTime = models.DateTimeField('更新时间', auto_now=True)
    

    def __str__(self):
        return self.tag
    
    def __unicode__(self):
        return self.tag
    
    def toDict(self):
        return {'tag': self.tag}
    
    class Meta:
        verbose_name = '标签'
        verbose_name_plural = verbose_name
        db_table = 'category'

class Course(models.Model):
    name = models.CharField('课程名称',max_length=32, unique=True, error_messages={'unique':'这个课程已存在'})
    type= models.IntegerField('类型',choices=COURSE_FORMAT_CHOICES,max_length=1,default=0)
    introdcution = models.CharField('课程介绍',max_length=128,blank=True,null=True)
    originPrice = models.IntegerField('原价',default=0)
    price = models.IntegerField('价格',default=0)
    category = models.ForeignKey(CourseCategoty,verbose_name='课程类别')
    filePath = models.ImageField(upload_to='upload',verbose_name='封面上传')
    tag = models.ManyToManyField(Tag,verbose_name='标签')
    likes = models.IntegerField('喜欢',default=0,editable=False)
    collect = models.IntegerField('收藏',default=0,editable=False)
    createTime = models.DateTimeField('创建时间',auto_now_add=True)
    updateTime = models.DateTimeField('更新时间', auto_now=True)
    


