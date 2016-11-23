from django.contrib import admin
from .models import Lesson, Course

# Register your models here.
class LessonInline(admin.TabularInline):
    model = Lesson
    fields = ['subject', 'description', 'order']
    extra = 0

class CourseAdmin(admin.ModelAdmin):
    list_display = ['name', 'short_description']
    search_fields = ['name']
    inlines = [LessonInline]

admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson)
admin.site.site_header = "PyBursa Administration"
