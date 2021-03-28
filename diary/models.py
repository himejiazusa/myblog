from django.db import models


class Dairy(models.Model):
    topic = models.CharField(max_length=200)

    def __str__(self):
        return self.topic