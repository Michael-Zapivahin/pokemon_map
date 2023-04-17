from django.db import models

class Pokemon(models.Model):
    title = models.TextField()
    image = models.ImageField(blank=True)

    def __str__(self):
        return self.title


class PokemonEntity(models.Model):
    lat = models.FloatField()
    lon = models.FloatField()

    def __str__(self):
        return f'lat: {self.lat}, lon: {self.lon}'




