# -*-coding:utf-8 -*-
'''
Created on 2013-10-15

@author: Danny<manyunkai@hotmail.com>
DannyWork Project
'''

from django.contrib import admin
from user.models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'acct_status',
                    'acct_identity', 'date_joined')

    def acct_status(self, user):
        if not user.is_active:
            return u'尚未激活'
        elif user.is_locked():
            return u'临时锁定'
        return u'正常'
    acct_status.short_description = u'账户状态'

    def acct_identity(self, user):
        if user.is_superuser:
            return u'超级管理员'
        elif user.is_staff:
            return u'管理员'
        return u'普通账户'
    acct_identity.short_description = u'账户身份'

admin.site.register(User, UserAdmin)
