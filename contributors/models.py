from django.db import models
from django.shortcuts import reverse

# ROLE_CHOICES = (
#     ('as a developer', 'as a developer'),
#     ('as a designer', 'as a designer'),
#     ('as a documentation team', 'as a documentation team'),
# )

# CONTRIBUTION_CHOICES = (
#     ('Developer', 'Developer'),
#     ('UX-designer', 'UX-designer'),
    # ('Front-end Designer', 'Front end designer'),
    # ('Database handler', 'Database handler'),
    # ('Back-end developer', 'Back-end developer'),
    # ('Project management', 'Project management'),
    # ('Xyz', 'Xyz'),
# )
# ROLE_CHOICES = (
#     ('as a developer', 'as a developer'),
#     ('as a designer', 'as a designer'),
#     ('as a documentation team', 'as a documentation team'),
# )

#
# class Contribution(models.Model):
#     contribution = models.CharField(max_length=30, choices=CONTRIBUTION_CHOICES)
#
#     def __str__(self):
#         return self.contribution

ROLE_CHOICES = (
    ('developer', 'developer'),
    ('designer', ' designer'),
    ('documentation team', 'documentation team'),
)


class CreateContributor(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    phone = models.CharField(max_length=13)
    # role = models.CharField(max_length=50)
    role = models.CharField(choices=ROLE_CHOICES, max_length=25)
    resume = models.FileField(upload_to='resumes')
    contributed = models.BooleanField(default=False)
    profession = models.CharField(max_length=255, default="Developer")
    about = models.CharField(max_length=255, default="working as software developer")

    def __str__(self):
        return self.name
