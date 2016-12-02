from django import forms
from .models import Course, Lesson

class CourseModelForm(forms.ModelForm):
    class Meta:
        model = Course
        exclude = 0

class LessonModelForm(forms.ModelForm):
    class Meta:
        model = Lesson
        exclude = 0
