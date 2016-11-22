from django.shortcuts import render
from .models import Course, Lesson
from students.models import Student
# Create your views here.

def detail(request, course_id):
    qs = Course.objects.get(id=course_id)
    leson = Lesson.objects.filter(course=qs)

    return render(request, 'courses/detail.html', {'course': qs, 'lessons': leson})