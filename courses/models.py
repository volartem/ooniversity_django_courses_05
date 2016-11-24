from django.db import models

class Course(models.Model):
    """
    -  name                         (CharField)     # название
    -  short_description            (CharField)     # краткое описание
    -  description                  (TextField)     # полное описание
    """
    name = models.CharField(max_length=60)
    short_description = models.CharField(max_length=255)
    description = models.TextField(default=None)

    def __str__(self):
        return self.name

class Lesson(models.Model):
    """
    -  subject                    (CharField)                          # тема
    -  description                (TextField)                          # описание
    -  course                     (ForeignKey на Course)               # курс
    -  order                      (PositiveIntegerField)               # номер по порядку
    """
    subject = models.CharField(max_length=60, )
    description = models.TextField(max_length=255)
    course = models.ForeignKey(Course)
    order = models.PositiveIntegerField()

    def __str__(self):
        return self.subject

    def __repr__(self):
        return self.subject