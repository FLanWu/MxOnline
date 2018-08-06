# _*_ coding: utf-8 _*_
__author__ = 'hcfly'
__date__ = '18-8-1 下午5:18'

from .models import *
import xadmin


class CourseAdmin(object):
    list_display = ['name', 'desc', 'detail', 'degree', 'learn_times', 'students',
                    'fav_num', 'image', 'click_nums', 'add_time']
    search_fields = ['name', 'desc', 'detail', 'degree', 'students',
                    'fav_num', 'image', 'click_nums', 'add_time']
    list_filter = ['name', 'desc', 'detail', 'degree', 'learn_times', 'students',
                    'fav_num', 'image', 'click_nums', 'add_time']


xadmin.site.register(Course, CourseAdmin)


class LessonAdmin(object):
    list_display = ['course', 'name', 'add_time']
    search_fields = ['course', 'name']
    list_filter = ['course__name', 'name', 'add_time']
    # 引用外键的里面的字段后为classname__dataname方式


xadmin.site.register(Lesson, LessonAdmin)


class VideoAdmin(object):
    list_display = ['lesson', 'name', 'add_time']
    search_fields = ['lesson', 'name']
    list_filter = ['lesson', 'name', 'add_time']


xadmin.site.register(Video, VideoAdmin)


class CourseResourceAdmin(object):
    list_display = ['course', 'name', 'download', 'add_time']
    search_fields = ['course', 'name', 'download']
    list_filter = ['course', 'name', 'download', 'add_time']


xadmin.site.register(CourseResource, CourseResourceAdmin)

