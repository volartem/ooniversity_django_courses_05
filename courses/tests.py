from django.test import TestCase, Client
from .models import Course, Lesson
from coaches.models import Coach
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User


class CoursesListTest(TestCase):
    def test_index_view_with_no_questions(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

    def test_course_create(self):
        course = Course.objects.create(
            name='Some Course',
            short_description='Short description',
            description='Default',
        )
        self.assertEquals(Course.objects.all().count(), 1)

    def test_page(self):
        client = Client()
        response = client.get('/courses/1/')
        self.assertEqual(response.status_code, 404)

    def test_valid_link_main(self):
        response = self.client.get('/')
        self.assertContains(response, 'Главная')

    def test_valid_link_contacts(self):
        response = self.client.get('/')
        self.assertContains(response, 'Контакты')

    def test_valid_link_students(self):
        response = self.client.get('/')
        self.assertContains(response, 'Студенты')


class CoursesDetailTest(TestCase):
    def create_lesson(self, course, order):
        lesson = Lesson.objects.create(
            subject='Name of Lesson',
            description='Description of Lesson',
            course=course,
            order=order,
        )
        return lesson

    def test_course_detail(self):
        course1 = Course.objects.create(
            name='Some Course',
            short_description='Short description',
            description='Default',
        )
        response = self.client.get('/courses/1/')
        self.assertContains(response, course1.name)

    def test_course_detail_response(self):
        course = Course.objects.create(
            name='Some Course',
            short_description='Short description',
            description='Default',
        )
        response = self.client.get('/courses/1/')
        self.assertEqual(response.status_code, 200)

    def test_list_lessons_course(self):
        course = Course.objects.create(
            name='Some Course',
            short_description='Short description',
            description='Default',
        )
        lesson1 = self.create_lesson(course, 1)
        lesson2 = self.create_lesson(course, 2)
        client = Client()
        response = client.get('/courses/1/')
        self.assertContains(response, lesson1.subject and lesson2.subject)

    def test_add_lesson_link(self):
        course = Course.objects.create(
            name='Some Course',
            short_description='Short description',
            description='Default',
        )
        response = self.client.get('/courses/{0}/'.format(course.id))
        self.assertContains(response, '/courses/{0}/add_lesson'.format(course.id))

    def test_coach_course(self):
        user = User(first_name='Ivan', last_name='Ivanov')
        user.save()
        coach = Coach.objects.create(
            user=user,
            date_of_birth='2000-01-02',
            gender='M',
            phone=12345678,
            address='Kharkov',
            skype='ivan',
            description='Good coach',
        )
        course = Course.objects.create(
            name='Some Course',
            short_description='Short description',
            description='Default',
            coach=coach,
        )
        response = self.client.get('/courses/{}/'.format(course.id))
        self.assertContains(response, '/coaches/{}/'.format(coach.id))