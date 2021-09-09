# Python Imports
import uuid

# Django imports
from django.core.validators import RegexValidator
from django.db import models
from django.contrib.auth.models import AbstractUser

# Locals Imports
from .typeUsers import TypeUser


class User(AbstractUser):
    """
    Class User extend  Abstract User
    """
    typeUser = models.ForeignKey(TypeUser, on_delete=models.CASCADE, null=True)
    unique_code = models.UUIDField('Code Unique Generate', default=uuid.uuid4, editable=False)
    email = models.EmailField('email address', unique=True)
    first_name = models.CharField('First Name', max_length=255, blank=False, null=False)
    last_name = models.CharField('Last Name', max_length=255, blank=False, null=False)
    identify = models.CharField('identify user', max_length=255, blank=False, null=True, unique=True)
    phone_regex = RegexValidator(
        regex=r'\+?1?\d{9,15}$',
        message="Phone number must be entered in the format: +999999999. Up to 15 digits allowed."
    )
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email
