from django.db import models


class Item(models.Model):
    """List element."""
    text = models.TextField(default='')
