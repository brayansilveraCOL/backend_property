# Python Imports
import uuid

# Django imports
from django.db import models

# Local imports
from backend_property.utils.classes.BaseAbstractModel import BaseModel


class TypeProperty(BaseModel):
    unique_code = models.UUIDField('Code Unique Generate', default=uuid.uuid4, editable=False)
    description = models.CharField(max_length=255)
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name
