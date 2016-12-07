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

class StudentEditView(UpdateView):
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

# def list_view(request):
#     try:
#         cours = Course.objects.get(id=int(request.GET.get('course_id')))
#         students = Student.objects.filter(courses=cours)
#     except TypeError:
#         students = Student.objects.all()
#     return render(request, "students/list.html", {"students": students})
#
#
# def detail(request, student_id):
#     student = get_object_or_404(Student, id=int(student_id))
#     return render(request, "students/detail.html", {"student": student})
#
#
# def create(request):
#     if request.method == 'POST':
#         model_form = StudentModelForm(request.POST)
#         if model_form.is_valid():
#             model_form.save()
#             messages.success(request, 'Student {0} {1} has been successfully added'.format(
#                                                             model_form.cleaned_data['name'],
#                                                             model_form.cleaned_data['surname']))
#             return redirect('students:list_view')
#     else:
#         model_form = StudentModelForm()
#     return render(request, "students/add.html", {"model": model_form})
#
# def edit(request, student_id):
#     student = Student.objects.get(id=int(student_id))
#     if request.method == 'POST':
#         model_form = StudentModelForm(request.POST, instance=student)
#         if model_form.is_valid():
#             model_form.save()
#             messages.success(request, 'Info on the student has been successfully changed.')
#             return redirect('students:edit', student_id)
#     else:
#         model_form = StudentModelForm(instance=student)
#     return render(request, 'students/edit.html', {"model": model_form})
#
# def remove(request, student_id):
#     student = Student.objects.get(id=int(student_id))
#     if request.method == 'POST':
#         student.delete()
#         messages.success(request, 'Info on {0} {1} has been successfully deleted.'.format(student.name, student.surname))
#         return redirect('students:list_view')
#     else:
#         return render(request, 'students/remove.html', {"model": student})
