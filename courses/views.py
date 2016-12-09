from django.shortcuts import render, redirect
from .models import Course, Lesson
from .forms import CourseModelForm, LessonModelForm
from django.contrib import messages
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy, reverse

class CourseDetailView(DetailView):
    model = Course
    template_name = 'courses/detail.html'

    def get_queryset(self):
        qs = super().get_queryset()
        cours_id = self.request.GET.get('pk', None)
        if cours_id:
            qs = qs.filter(courses=cours_id)
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['lessons'] = Lesson.objects.filter(course=self.get_queryset())
        return context

class CourseCreateView(CreateView):
    model = Course
    form_class = CourseModelForm
    template_name = 'courses/add.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Course %s has been successfully added.' %
                         form.instance.name)
        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Course creation'
        return context

class CourseUpdateView(UpdateView):
    model = Course
    form_class = CourseModelForm
    template_name = 'courses/edit.html'

    def get_success_url(self):
        return reverse('courses:edit', args=(self.object.pk,))

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'The changes have been saved.')
        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Course update'
        return context

class CourseDeleteView(DeleteView):
    model = Course
    template_name = 'courses/remove.html'
    success_url = reverse_lazy('index')

    def delete(self, request, *args, **kwargs):
        response = super().delete(request, *args, **kwargs)
        messages.success(self.request, 'Course %s has been deleted.' %
                         self.object.name)
        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Course deletion'
        return context


def add_lesson(request, course_id):
    # course = Course.objects.get(id=int(course_id))
    if request.method == 'POST':
        model_form = LessonModelForm(request.POST)
        if model_form.is_valid():
            model_form.save()
            messages.success(request, 'Lesson {0} has been successfully added.'.format(model_form.cleaned_data['subject']))
            return redirect('/courses/{0}/'.format(course_id))
    else:
        model_form = LessonModelForm(initial={'course': int(course_id)})
    return render(request, 'courses/add_lesson.html', {'model': model_form})

def edit_lesson(request, lesson_id):
    lesson = Lesson.objects.get(id=int(lesson_id))
    if request.method == 'POST':
        model_form = LessonModelForm(request.POST, instance=lesson)
        if model_form.is_valid():
            model_form.save()
            messages.success(request, 'The changes have been saved.')
            return redirect('/courses/{0}/edit_lesson'.format(lesson_id))
    else:
        model_form = LessonModelForm(instance=lesson)
    return render(request, 'courses/edit_lesson.html', {'model': model_form})

def remove_lesson(request, lesson_id):
    lesson = Lesson.objects.get(id=int(lesson_id))
    if request.method == 'POST':
        lesson.delete()
        messages.success(request, 'Lesson {0} has been deleted.'.format(lesson.subject))
        return redirect('/courses/{0}/'.format(lesson.course.id))
    else:
        model_form = LessonModelForm(instance=lesson)
    return render(request, 'courses/remove_lesson.html', {'model': model_form})