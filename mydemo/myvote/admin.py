from django.contrib import admin

# Register your models here.

# 导入模型
from .models import *

# 注册Questions模型类
admin.site.register(Questions)


class ChoiceAdmin(admin.ModelAdmin):
    list_display = ["title","question","votesnum"]

# 注册Choice模型类
admin.site.register(Choice,ChoiceAdmin)