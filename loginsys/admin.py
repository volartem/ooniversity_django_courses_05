from django.contrib import admin
from .models import TempUserProfile
# Register your models here.

class LoginsysAdmin(admin.ModelAdmin):
    readonly_fields = ('key_expires',)

admin.site.register(TempUserProfile, LoginsysAdmin)
