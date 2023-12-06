from django.db import models

class TeamMember(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    phone_number = models.CharField(max_length=13)
    email = models.EmailField()
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('regular', 'Regular'),
    )
    role = models.CharField(max_length=7, choices=ROLE_CHOICES, default='regular')

    def __str__(self):
        return self.name