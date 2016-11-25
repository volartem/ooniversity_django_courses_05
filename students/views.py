from django.shortcuts import render

from .models import Student
from courses.models import Course
# Create your views here.

def list_view(request):
    try:
        cours = Course.objects.get(id=int(request.GET.get('course_id')))
        students = Student.objects.filter(courses=cours)
    except TypeError:
        students = Student.objects.all()
    return render(request, "students/list.html", {"students": students})


def detail(request, stud_id):
    student = Student.objects.get(id=int(stud_id))
    return render(request, "students/detail.html", {"student": student})