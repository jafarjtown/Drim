from django.db import models
import uuid
# Create your models here.

class ModelHelper(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_created=True)

    class Meta:
        abstract = True