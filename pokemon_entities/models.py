from django.db import models

class Pokemon(models.Model):
    title = models.TextField()
    image = models.ImageField(blank=True)

    def __str__(self):
        return self.title



