from django.contrib import admin

# Register your models here.
from django.contrib import admin
from login.models import SiteUser

from login.models import ConfirmString


# Register your models here.

# 后台管理设置的信息
class SiteUserAdmin(admin.ModelAdmin):
    list_display = ['name', 'gender', 'email']
    list_display_links = ['name']
    list_filter = ['gender', 'create_time']
    list_per_page = 10
admin.site.register(SiteUser, SiteUserAdmin)
admin.site.site_header = 'ChatGPT-Pdf-Upload系统'
admin.site.site_title = 'ChatGPT-Pdf-Upload系统'
admin.site.register(ConfirmString)