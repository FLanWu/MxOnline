# _*_ coding: utf-8 _*_
__author__ = 'hcfly'
__date__ = '18-8-1 下午6:00'

import xadmin

from .models import *


class UserAskAdmin(object):
    list_display = ['name', 'mobile', 'course_name', 'add_time']
    search_fields = ['name', 'mobile', 'course_name']
    list_filter = ['name', 'mobile', 'course_name', 'add_time']


xadmin.site.register(UserAsk, UserAskAdmin)


class CourseCommentsAdmin(object):
    list_display = ['user', 'comments', 'course', 'add_time']
    search_fields = ['user', 'comments', 'course']
    list_filter = ['user', 'comments', 'course', 'add_time']


xadmin.site.register(CourseComments, CourseCommentsAdmin)


class UserFavoriteAdmin(object):
    list_display = ['user', 'fav_id', 'fav_type', 'add_time',]
    search_fields = ['user', 'fav_id', 'fav_type']
    list_filter = ['user', 'fav_id', 'fav_type', 'add_time',]


xadmin.site.register(UserFavorite, UserFavoriteAdmin)


class UserMessageAdmin(object):
    list_display = ['user', 'message', 'has_read', 'add_time']
    search_fields = ['user', 'message', 'has_read']
    list_filter = ['user', 'message', 'has_read', 'add_time']


xadmin.site.register(UserMessage, UserMessageAdmin)


class UserCourseAdmin(object):
    list_display = ['user', 'course', 'add_time']
    search_fields = ['user', 'course']
    list_filter = ['user', 'course', 'add_time']


xadmin.site.register(UserCourse, UserCourseAdmin)




