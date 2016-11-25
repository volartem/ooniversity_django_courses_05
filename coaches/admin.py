from django.contrib import admin
from .models import Coach
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
# Register your models here.

class CoachAdmin(admin.ModelAdmin):
    list_display = ['name', 'surname', 'gender', 'skype', 'description']
    list_filter = ['user__is_staff', ]

    def name(self, obj):
        return obj.user.first_name

    def surname(self, obj):
        return obj.user.last_name

admin.site.register(Coach, CoachAdmin)