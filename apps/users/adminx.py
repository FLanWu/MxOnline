# _*_ coding: utf-8 _*_
__author__ = 'hcfly'
__date__ = '18-7-31 下午4:51'


import xadmin
from .models import EmailVerifyRecord, Banner
from xadmin import views


class BaseSetting(object):
    # xadmin 的主题注册（全局）
    enable_themes = True
    # use_bootswatch = True


xadmin.site.register(views.BaseAdminView, BaseSetting)


class GlobalSettings(object):
    site_title = u'慕学管理系统'  # 修改左上角
    site_footer = u'慕学在线网'  # 修改页面底部@
    menu_style = 'accordion'   #  左侧菜单折叠


xadmin.site.register(views.CommAdminView, GlobalSettings)


class EmailVerifyRecordAmdin(object):
    list_display = ['code', 'email', 'send_type', 'send_time']
    search_fields = ['code', 'email', 'send_type']
    list_filter = ['code', 'email', 'send_type', 'send_time']


xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAmdin)


class BannerAdmin(object):
    list_display = ['title', 'image', 'url', 'index', 'add_time']
    search_fields = ['title', 'image', 'url', 'index']
    list_filter = ['title', 'image', 'url', 'index', 'add_time']


xadmin.site.register(Banner, BannerAdmin)


# class UserProfileAdmin(object):
#     list_display = ['nick_name', 'birday', 'gender', 'address', 'mobile', 'image']
#     search_fields = ['nick_name', 'birday', 'gender', 'address', 'mobile']
#     list_filter = ['nick_name', 'birday', 'gender', 'address', 'mobile', 'image']
#
# xadmin.site.unregister(UserProfile)
# xadmin.site.register(UserProfile, UserProfileAdmin)


