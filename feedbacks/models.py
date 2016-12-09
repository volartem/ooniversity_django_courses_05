from django.db import models


class Feedback(models.Model):
    name = models.CharField(max_length=16)
    subject = models.CharField(max_length=60)
    message = models.TextField()
    from_email = models.EmailField()
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject