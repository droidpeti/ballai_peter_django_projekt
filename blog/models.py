from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    rendelo = models.CharField(max_length=50)
    pizza = models.CharField(max_length=255, default="Marghareita")
    italok = models.TextField( null=True, max_length=255, default="Coca Cola")
    leadott_datum = models.DateTimeField(
            default=timezone.now)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.pizza
