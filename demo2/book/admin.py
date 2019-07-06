from django.contrib import admin

# Register your models here.

# 导入模型
from .models import *

# 实现关联注册，添加书籍时，可以直接添加新的英雄信息
class HeroInfoInline(admin.StackedInline):
    model = HeroInfo
    # 添加关联英雄的个数
    extra = 1

# 重写Django后台，可以自定义模型的管理器
class BookInfoAdmin(admin.ModelAdmin):
    # 显示定义的部分字段信息
    list_display = ("title",)
    # 添加书籍的同时，可以添加新的英雄信息
    inlines = [HeroInfoInline]

# 注册BookInfo模型类
admin.site.register(BookInfo,BookInfoAdmin)


class HeroInfoAdmin(admin.ModelAdmin):
    list_display = ["name","sex","skill","book"]

# 注册HeroInfo模型类
admin.site.register(HeroInfo,HeroInfoAdmin)