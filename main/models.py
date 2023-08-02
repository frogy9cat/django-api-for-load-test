from django.db import models


class Counter(models.Model):
    icounter = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

