from django.db import models

# Create your models here.
class Memory(models.Model):
    query=models.CharField(max_length=500)
    reply=models.TextField(blank=True)

    class Meta:
        ordering=("query",)
