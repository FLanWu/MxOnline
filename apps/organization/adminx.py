# _*_ coding: utf-8 _*_
__author__ = 'hcfly'
__date__ = '18-8-1 下午5:49'

import xadmin
from .models import CityDict, CourseOrg, Teacher


class CityDictAdmin(object):
    list_display = ['name', 'desc', 'add_time']
    search_fields = ['name', 'desc']
    list_filter = ['name', 'desc', 'add_time']


xadmin.site.register(CityDict, CityDictAdmin)


class CourseOrgAdmin(object):
    list_display = ['name', 'desc', 'add_time', 'click_num', 'fav_nums', 'image', 'address', 'city']
    search_fields = ['name', 'desc', 'click_num', 'fav_nums', 'image', 'address', 'city']
    list_filter = ['name', 'desc', 'add_time', 'click_num', 'fav_nums', 'image', 'address', 'city']


xadmin.site.register(CourseOrg, CourseOrgAdmin)


class TeacherAdmin(object):
    list_display = ['org', 'name', 'work_years', 'work_company', 'work_position',
                    'points', 'click_num', 'fav_nums', 'add_time']
    search_fields = ['org', 'name', 'work_years', 'work_company', 'work_position',
                    'points', 'click_num', 'fav_nums']
    list_filter = ['org', 'name', 'work_years', 'work_company', 'work_position',
                    'points', 'click_num', 'fav_nums', 'add_time']


xadmin.site.register(Teacher, TeacherAdmin)