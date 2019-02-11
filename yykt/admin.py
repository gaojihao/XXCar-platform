from django.contrib import admin
from yykt.models import *
from markdownx.admin import AdminMarkdownxWidget
from django.utils.safestring import mark_safe



admin.site.site_header = 'xx课堂'
admin.site.site_title = 'zz系统'
admin.site.index_title = 'yy课堂'
admin.site.site_url = ''

admin.site.disable_action('delete_selected')


class CourseAdmin(admin.ModelAdmin):
    list_display = ['name','category','status','filePath_data','price','studyPeople']
    #list_per_page设置每页显示多少条记录，默认是100条
    list_per_page = 50
    #筛选器
    list_filter =('category', 'status', 'level') #过滤器
    search_fields =('name', 'category') #搜索字段
    date_hierarchy = 'createTime'    #筛选
    readonly_fields = ['filePath_data']

    def filePath_data(self, obj):
        return mark_safe('<img src="%s" width="100px" height="60px"/>' % ('http://127.0.0.1:8000'+obj.filePath.url))
    filePath_data.short_description = '封面图片'


class UserAdmin(admin.ModelAdmin):
    list_display = ['phone','nickName','realName','wechatNum','childName','birthday']
    readonly_fields = ('phone','password','nickName','realName','uniqueId','wechatNum','childName','birthday','childSex')

    def has_add_permission(self,request):
        return False

class CollectAdmin(admin.ModelAdmin):
    list_display = ['course','user','createTime','updateTime']
    readonly_fields = ('course','user','createTime','updateTime')

    def has_add_permission(self,request):
        return False

class LikeAdmin(admin.ModelAdmin):
    list_display = ['course','user','createTime','updateTime']
    readonly_fields = ('course','user','createTime','updateTime')

    def has_add_permission(self,request):
        return False

class CommentAdmin(admin.ModelAdmin):
    list_display = ['course','user','comment','level']
    readonly_fields = ('course','user','comment','level')

    def has_add_permission(self,request):
        return False

class VideoAdmin(admin.ModelAdmin):
    list_display = ['name','course','createTime','updateTime']
    

class AudioAdmin(admin.ModelAdmin):
    list_display = ['name','course','createTime','updateTime']
    

class BannerAdmin(admin.ModelAdmin):
    pass

class ArticleAdmin(admin.ModelAdmin):
    formfield_overrides = {
        MarkdownxField: {'widget': AdminMarkdownxWidget}
    }


admin.site.register(CourseCategoty)
admin.site.register(Tag)
admin.site.register(Article,ArticleAdmin)
admin.site.register(Course,CourseAdmin)
admin.site.register(Video,VideoAdmin)
admin.site.register(Audio,AudioAdmin)
admin.site.register(User,UserAdmin)
admin.site.register(Collect,CollectAdmin)
admin.site.register(Like,LikeAdmin)
admin.site.register(Comment,CommentAdmin)
admin.site.register(Banner,BannerAdmin)