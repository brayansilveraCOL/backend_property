# Python Imports
import uuid

# Django Imports
from django.db import models

# Local imports
from backend_property.utils.classes.BaseAbstractModel import BaseModel
from .typeProperty import TypeProperty
from ...users.models import User


class Property(BaseModel):
    unique_code = models.UUIDField('Code Unique Generate', default=uuid.uuid4, editable=False)
    typeProperty = models.ForeignKey(TypeProperty, on_delete=models.CASCADE)
    identifyCatrastal = models.CharField(max_length=250, unique=True)
    address = models.CharField(max_length=250)
    name = models.CharField(max_length=250)
    identify = models.CharField(max_length=250, unique=True)
    users = models.ManyToManyField(User, null=True)
