from django.db import models
from django.urls import reverse


class List(models.Model):

    def get_absolute_url(self):
        """Get absolute url."""
        return reverse('view_list', args=[self.id])


class Item(models.Model):
    """List element."""
    text = models.TextField(default='')
    list = models.ForeignKey(List, default=None, on_delete=models.CASCADE)
