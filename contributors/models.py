from django.db import models


ROLE_CHOICES = (
    ('developer', 'developer'),
    ('designer', ' designer'),
    ('documentation team', 'documentation team'),
)


class CreateContributor(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    phone = models.CharField(max_length=13)
    resume = models.FileField(upload_to='resumes')
    contributed = models.BooleanField(default=False)
    role = models.CharField(choices=ROLE_CHOICES, max_length=25)
    about = models.CharField(max_length=255)

    def __str__(self):
        return self.name
