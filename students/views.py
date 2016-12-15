from .forms import StudentModelForm
from .models import Student
from django.contrib import messages
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy, reverse
import logging


logger = logging.getLogger('students')


class StudentListView(ListView):
    model = Student
    paginate_by = 2

    def get_queryset(self):
        qs = super().get_queryset()
        course_id = self.request.GET.get('course_id', None)
        if course_id:
            qs = qs.filter(courses=course_id)
        return qs
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        temp = self.request.GET.get('course_id')
        context['course_id'] = '?course_id=%s&' % temp if temp else '?'
        return context

class StudentDetailView(DetailView):
    model = Student
    logger.debug('Students detail view has been debugged!')
    logger.info('Logger of students detail view informs you!')
    logger.warning('Logger of students detail view warns you!')
    logger.error('Students detail view went wrong!')



class StudentCreateView(CreateView):
    model = Student
    form_class = StudentModelForm
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
    template_name_suffix = '_update_form'

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
