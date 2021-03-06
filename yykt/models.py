from django.db import models
from markdownx.models import MarkdownxField



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
        verbose_name = '分类管理'
        verbose_name_plural = verbose_name
        

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
        verbose_name = '标签管理'
        verbose_name_plural = verbose_name
        db_table = 'category'

class Course(models.Model):

    SALE_CHOICES = (
        (True, u'上架'),
        (False, u'下架'),
    )

    COURSE_FORMAT_CHOICES = (
    (0, u'视频'),
    (1, u'音频'),
    (3, u'文章'),
    )

    name = models.CharField('课程名称',max_length=32, unique=True, error_messages={'unique':'这个课程已存在'})
    sunTitle = models.CharField('子标题',max_length=64,blank=True,null=True)
    des = models.TextField('描述',blank=True,null=True)
    courseType= models.IntegerField('类型',choices=COURSE_FORMAT_CHOICES,default=0)
    introdcution = models.CharField('课程介绍',max_length=128,blank=True,null=True)
    originPrice = models.IntegerField('原价',default=0)
    price = models.IntegerField('价格',default=0)
    category = models.ForeignKey(CourseCategoty,verbose_name='课程类别',on_delete=models.CASCADE)
    filePath = models.ImageField(upload_to='upload',verbose_name='封面上传')
    tag = models.ManyToManyField(Tag,verbose_name='标签')
    status= models.BooleanField('上下架',choices=SALE_CHOICES,default=True)
    likeNum = models.IntegerField('喜欢',default=0,editable=False)
    collectNum = models.IntegerField('收藏',default=0,editable=False)
    studyPeople = models.IntegerField('学习人数',default=0,editable=False)
    level = models.FloatField('评分',default=5.0,editable=False)
    createTime = models.DateTimeField('创建时间',auto_now_add=True)
    updateTime = models.DateTimeField('更新时间', auto_now=True)

    def __str__(self):
        return self.name
    
    def __unicode__(self):
        return self.name
    
    class Meta:
        verbose_name = '课程管理'
        verbose_name_plural = verbose_name

class Video(models.Model):
    name = models.CharField('名称',max_length=32, unique=True, error_messages={'unique':'这个视频已存在'})
    course = models.ForeignKey(Course,verbose_name='课程名称',on_delete=models.CASCADE)
    
    filePath = models.FileField(upload_to='upload',verbose_name='视频上传',unique=True,error_messages={'unique':'这个视频已存在'})

    createTime = models.DateTimeField('创建时间',auto_now_add=True)
    updateTime = models.DateTimeField('更新时间', auto_now=True)

    def __str__(self):
        return self.name
    
    def __unicode__(self):
        return self.name
    
    class Meta:
        verbose_name = '视频课程'
        verbose_name_plural = verbose_name

class Audio(models.Model):
    name = models.CharField('名称',max_length=32, unique=True, error_messages={'unique':'这个音频已存在'})
    course = models.ForeignKey(Course,verbose_name='课程名称',on_delete=models.CASCADE)
    
    filePath = models.FileField(upload_to='upload',verbose_name='音频上传',unique=True,error_messages={'unique':'这个音频已存在'})

    createTime = models.DateTimeField('创建时间',auto_now_add=True)
    updateTime = models.DateTimeField('更新时间', auto_now=True)

    def __str__(self):
        return self.name
    
    def __unicode__(self):
        return self.name
    
    class Meta:
        verbose_name = '音频课程'
        verbose_name_plural = verbose_name

class Article(models.Model):
    title = models.CharField('标题',max_length=32, unique=True, error_messages={'unique':'这篇文章已存在'})
    myfield = MarkdownxField()
    createTime = models.DateTimeField('创建时间',auto_now_add=True)
    updateTime = models.DateTimeField('更新时间', auto_now=True)

    def __str__(self):
        return self.title
    
    def __unicode__(self):
        return self.title
    
    class Meta:
        verbose_name = '文章管理'
        verbose_name_plural = verbose_name

class User(models.Model):
    phone = models.CharField('手机号码',max_length=11, unique=True, error_messages={'unique':'这个用户已存在'})
    password = models.CharField('密码',max_length=256)
    nickName = models.CharField('昵称',max_length=16,null=True,blank=True)
    realName = models.CharField('真实姓名',max_length=16,null=True,blank=True)
    uniqueId = models.CharField('微信唯一标识',max_length=256,null=True,blank=True)
    wechatNum = models.CharField('微信号',max_length=16,null=True,blank=True)
    childName = models.CharField('子女姓名',max_length=8,null=True,blank=True)
    childSex = models.CharField('子女性别',max_length=1,null=True,blank=True)
    birthday = models.DateField('出生年月')
    createTime = models.DateTimeField('创建时间',auto_now_add=True)
    updateTime = models.DateTimeField('更新时间', auto_now=True)

    def __str__(self):
        return self.phone
    
    def __unicode__(self):
        return self.phone
    
    class Meta:
        verbose_name = '用户管理'
        verbose_name_plural = verbose_name

class Comment(models.Model):
    comment = models.CharField('内容',max_length=256)
    level = models.FloatField('评分',default=5.0,editable=False)
    course = models.ForeignKey(Course,verbose_name='课程名称',on_delete=models.CASCADE)
    user = models.ForeignKey(User,verbose_name='评论人',on_delete=models.CASCADE)
    createTime = models.DateTimeField('创建时间',auto_now_add=True)
    updateTime = models.DateTimeField('更新时间', auto_now=True)

    def __str__(self):
        return self.comment
    
    def __unicode__(self):
        return self.comment
    
    class Meta:
        verbose_name = '用户评论'
        verbose_name_plural = verbose_name

class Collect(models.Model):
    course = models.ForeignKey(Course,verbose_name='课程名称',on_delete=models.CASCADE)
    user = models.ForeignKey(User,verbose_name='用户',on_delete=models.CASCADE)
    createTime = models.DateTimeField('创建时间',auto_now_add=True)
    updateTime = models.DateTimeField('更新时间', auto_now=True)

    def __str__(self):
        return self.course.name
    
    def __unicode__(self):
        return self.course.name
    
    class Meta:
        verbose_name = '用户收藏'
        verbose_name_plural = verbose_name

class Like(models.Model):
    course = models.ForeignKey(Course,verbose_name='课程名称',on_delete=models.CASCADE)
    user = models.ForeignKey(User,verbose_name='用户',on_delete=models.CASCADE)
    createTime = models.DateTimeField('创建时间',auto_now_add=True)
    updateTime = models.DateTimeField('更新时间', auto_now=True)

    def __str__(self):
        return self.course.name
    
    def __unicode__(self):
        return self.course.name
    
    class Meta:
        verbose_name = '用户喜欢'
        verbose_name_plural = verbose_name

class Banner(models.Model):
    course = models.ForeignKey(Course,verbose_name='课程名称',on_delete=models.CASCADE)
    createTime = models.DateTimeField('创建时间',auto_now_add=True)
    updateTime = models.DateTimeField('更新时间', auto_now=True)

    def __str__(self):
        return self.course.name
    
    def __unicode__(self):
        return self.course.name
    
    class Meta:
        verbose_name = '广告位'
        verbose_name_plural = verbose_name
