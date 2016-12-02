from django.shortcuts import render, redirect
from .models import Course, Lesson
from .forms import CourseModelForm, LessonModelForm
from django.contrib import messages
# Create your views here.

def detail(request, course_id):
    qs = Course.objects.get(id=course_id)
    leson = Lesson.objects.filter(course=qs)

    return render(request, 'courses/detail.html', {'course': qs, 'lessons': leson})

def add(request):
    if request.method == 'POST':
        model_form = CourseModelForm(request.POST)
        if model_form.is_valid():
            model_form.save()
            messages.success(request, "Course {0} has been successfully added.".format(model_form.cleaned_data['name']))
            return redirect('/')
    else:
        model_form = CourseModelForm()
    return render(request, 'courses/add.html', {'model': model_form})

def add_lesson(request, course_id):
    if request.method == 'POST':
        model_form = LessonModelForm(request.POST)
        if model_form.is_valid():
            model_form.save()
            messages.success(request, 'Lesson {0} has been successfully added'.format(model_form.cleaned_data['subject']))
            return redirect('/courses/{0}/'.format(course_id))
    else:
        model_form = LessonModelForm(initial={'course': course_id})
    return render(request, 'courses/add_lesson.html', {'model': model_form})


def edit(request, course_id):
    course = Course.objects.get(id=int(course_id))
    if request.method == 'POST':
        model_form = CourseModelForm(request.POST, instance=course)
        if model_form.is_valid():
            model_form.save()
            messages.success(request, 'The changes have been saved.')
            return redirect('/courses/edit/{0}/'.format(course_id))
    else:
        model_form = CourseModelForm(instance=course)
    return render(request, 'courses/edit.html', {'model': model_form})

def remove(request, course_id):
    course = Course.objects.get(id=int(course_id))
    if request.method == 'POST':
        course.delete()
        messages.success(request, 'Course {0} has been deleted.'.format(course.name))
        return redirect('/')
    else:
        model_form = CourseModelForm(instance=course)
    return render(request, 'courses/remove.html', {'model': model_form})


