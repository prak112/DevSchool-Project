from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class UserProfile(AbstractUser):
    USER_CHOICES = [
        ('ART', 'Art'),
        ('PHT', 'Photography'),
        ('ENT', 'Curiosity')
    ]

    # AbstractUser model fields - username, first_name, last_name, email, username, password, is_staff, is_active, date_joined
    # define additional or custom fields
    customer_type = models.CharField('Interested in ?', max_length=20, choices=USER_CHOICES)
    bio = models.TextField('Bio', max_length=200, null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}".capitalize()


# OMITTED CODE - Purpose - SIMPLIFICATION 

    # login_name = models.CharField('Username (auto-generated)', max_length=150, unique=True, null=True)

    # define related_name to resolve clashes with User module
    # groups = models.ManyToManyField('auth.Group', related_name='userprofile')
    # user_permissions = models.ManyToManyField('auth.Permission', related_name='userprofile')

    # def save_login_name(self, *args, **kwargs):
    #     """
    #     Saves the current object to the database.

    #     This method generates a unique username for the object by combining the lowercase
    #     first name and last name with a random 4-digit suffix. The generated username is
    #     then assigned to the `username` attribute of the object.
    #     """
    #     import random

    #     suffix = str(random.randint(1000, 9999))
    #     self.login_name = f"{self.fname.lower()}{self.lname.lower()}_{suffix[:4]}"
    #     super().save_login_name(*args, **kwargs)

