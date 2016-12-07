from django.shortcuts import render, redirect, get_object_or_404
from .forms import StudentModelForm
from .models import Student
from courses.models import Course
from django.contrib import messages
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy, reverse


class StudentListView(ListView):
    model = Student
    template_name = 'students/list.html'
    context_object_name = 'students'

    def get_queryset(self):
        qs = super().get_queryset()
        cours_id = self.request.GET.get('course_id', None)
        if cours_id:
            qs = qs.filter(courses=cours_id)
        return qs

class StudentDetailView(DetailView):
    model = Student
    template_name = 'students/detail.html'

class StudentCreateView(CreateView):
    model = Student
    form_class = StudentModelForm
    template_name = 'students/add.html'
    success_url = reverse_lazy('students:list_view')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Student %s %s has been successfully added' %
                         (form.instance.name, form.instance.surname))
        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Student registration'
        return context

class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentModelForm
    template_name = 'students/edit.html'
    # context_object_name = 'model'

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Info on the student has been successfully changed.')
        return response

    def get_success_url(self):
        return reverse('students:edit', args=(self.object.pk,))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Student info update'
        return context

class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'students/remove.html'
    # context_object_name = 'student'
    success_url = reverse_lazy('students:list_view')

    def delete(self, request, *args, **kwargs):
        response = super().delete(request, *args, **kwargs)
        messages.success(self.request, 'Info on %s %s has been successfully deleted.' %
                         (self.object.name, self.object.surname))
        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Student info suppression'
        return context
