from django.db import models

# Create your models here.
class Course(models.Model):
    name = models.CharField(verbose_name="Course", max_length=60)
    short_description = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name
class Lesson(models.Model):
    subject = models.CharField(max_length=60)
    description = models.TextField(max_length=255)
    course = models.ForeignKey(Course)
    order = models.PositiveIntegerField()

    def __str__(self):
        return self.subject