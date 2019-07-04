from django.contrib import admin

# 导入模型
from .models import *

# Django自带的强大后台管理
# Register your models here.

# 实现关联注册，添加书籍时，可以直接添加新的英雄信息
class HeroInfoInline(admin.StackedInline):
    model = HeroInfo
    # 添加关联英雄的个数
    extra = 1

# 重写Django后台，可以自定义模型的管理器
class BookInfoAdmin(admin.ModelAdmin):
    # 显示定义的部分字段信息
    list_display = ("title","pub_date")
    # 添加过滤条件字段,过滤框会出现在右侧
    list_filter = ["title"]
    # 添加title作为搜索条件字段，搜索框会出现在上侧
    search_fields = ["title"]
    # 分页展示数据，分页框会出现在下侧
    list_per_page = 2
    # 添加书籍的同时，可以添加新的英雄信息
    inlines = [HeroInfoInline]


# 注册BookInfo模型类
admin.site.register(BookInfo,BookInfoAdmin)


class HeroInfoAdmin(admin.ModelAdmin):
    list_display = ["name","gender","content","book"]

    # 添加title和content作为搜索条件字段，book外键
    search_fields = ["name","content"]
    # 添加过滤条件字段
    list_filter = ["name","book"]
    # 添加name作为搜索条件字段
    search_fields = ["name"]


# 注册HeroInfo模型类
admin.site.register(HeroInfo,HeroInfoAdmin)