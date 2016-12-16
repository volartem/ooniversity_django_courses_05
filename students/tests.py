from django.test import TestCase, Client
from .models import Student
from courses.models import Course
from django.core.urlresolvers import reverse


class StudentsListTest(TestCase):
    def test_list_students(self):
        response = self.client.get(reverse('students:list_view'))
        self.assertEqual(response.status_code, 200)

    def test_course_create(self):
        student = Student.objects.create(
            name='Ivan',
            surname='Ivanov',
            date_of_birth='2000-01-01',
            email='test@email.com',
            phone=123456789,
            address='New York',
            skype='name_surname',
        )
        self.assertEquals(Student.objects.all().count(), 1)

    def test_student_add(self):
        response = self.client.get('/students/')
        self.assertContains(response, '/students/add/')

    def test_valid_links(self):
        response = self.client.get('/students/')
        self.assertContains(response, 'Главная')
        self.assertContains(response, 'Контакты')
        self.assertContains(response, 'Студенты')

    def test_student_link(self):
        student = Student.objects.create(
            name='Ivan',
            surname='Ivanov',
            date_of_birth='2000-01-01',
            email='test@email.com',
            phone=123456789,
            address='San Francisko',
            skype='name_surname',
        )

        response = self.client.get('/students/')
        self.assertContains(response, '/students/{}/'.format(student.id))

    def test_course_link(self):
        student = Student.objects.create(
            name='Ivan',
            surname='Ivanov',
            date_of_birth='2000-01-01',
            email='test@email.com',
            phone=123456789,
            address='Kharkov',
            skype='name_surname',
        )
        course = student.courses.create(
            name='Some Course',
            short_description='Short description',
            description='Default', )
        response = self.client.get('/students/')
        self.assertContains(response, '/courses/{}/'.format(course.id))


class StudentsDetailTest(TestCase):
    def test_students_full_name(self):
        student = Student.objects.create(
            name='Ivan',
            surname='Ivanov',
            date_of_birth='2000-01-01',
            email='test@email.com',
            phone=123456789,
            address='Moscow',
            skype='name_surname',
        )
        response = self.client.get('/students/{0}/'.format(student.id))
        self.assertContains(response, student.full_name)

    def test_students_valid_info(self):
        student = Student.objects.create(
            name='Ivan',
            surname='Ivanov',
            date_of_birth='2000-01-01',
            email='test@email.com',
            phone=123456789,
            address='London',
            skype='name_surname',
        )
        response = self.client.get('/students/{0}/'.format(student.id))
        self.assertContains(response, 'дата рождения')
        self.assertContains(response, 'адрес')
        self.assertContains(response, 'почта')
        self.assertContains(response, 'телефон')
        self.assertContains(response, 'логин skype')

    def test_students_courses(self):
        student = Student.objects.create(
            name='Ivan',
            surname='Ivanov',
            date_of_birth='2000-01-01',
            email='test@email.com',
            phone=123456789,
            address='Milan',
            skype='name_surname',
        )
        course1 = student.courses.create(
            name='Some Course',
            short_description='Short description',
            description='Default',)
        course2 = student.courses.create(
            name='Some Course2',
            short_description='Short description2',
            description='Default2', )
        response = self.client.get('/students/{0}/'.format(student.id))
        self.assertContains(response, '/courses/{0}/'.format(course1.id))
        self.assertContains(response, '/courses/{0}/'.format(course2.id))
        self.assertEqual(student.courses.all()[0], course1)
        self.assertEqual(student.courses.all()[1], course2)

    def test_pages_student_detail(self):
        student = Student.objects.create(
            name='Ivan',
            surname='Ivanov',
            date_of_birth='2000-01-01',
            email='test@email.com',
            phone=123456789,
            address='Moscow',
            skype='name_surname',
        )
        response = self.client.get('/students/1/')
        self.assertEqual(response.status_code, 200)

    def test_valid_links(self):
        student = Student.objects.create(
            name='Ivan',
            surname='Ivanov',
            date_of_birth='2000-01-01',
            email='test@email.com',
            phone=123456789,
            address='Moscow',
            skype='name_surname',
        )
        response = self.client.get('/students/1/')
        self.assertContains(response, 'Главная')
        self.assertContains(response, 'Контакты')
        self.assertContains(response, 'Студенты')