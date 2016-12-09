from django.contrib import admin
from .models import Feedback


class FeedbackAdmin(admin.ModelAdmin):
    readonly_fields = ('create_date',)
    fields = ('from_email', 'create_date')


admin.site.register(Feedback, FeedbackAdmin)