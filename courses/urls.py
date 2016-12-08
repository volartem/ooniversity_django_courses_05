from django.conf.urls import url, include
from . import views

app_name = 'courses'
urlpatterns = [
    url(r'^(?P<pk>\d+)/$', views.CourseDetailView.as_view(), name='detail'),
    url(r'^add/$', views.CourseCreateView.as_view(), name='add'),
    url(r'^edit/(?P<pk>\d+)/$', views.CourseUpdateView.as_view(), name='edit'),
    url(r'^remove/(?P<pk>\d+)/$', views.CourseDeleteView.as_view(), name='remove'),
    url(r'^(?P<course_id>\d+)/add_lesson$', views.add_lesson, name='add-lesson'),
    url(r'^(?P<lesson_id>\d+)/remove_lesson$', views.remove_lesson, name='remove-lesson'),
    url(r'^(?P<lesson_id>\d+)/edit_lesson$', views.edit_lesson, name='edit-lesson')
]