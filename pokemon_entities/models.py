from django.db import models

class Pokemon(models.Model):
    title = models.TextField()
    image = models.ImageField(blank=True)

    def __str__(self):
        return self.title


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(Pokemon, blank=True, on_delete=models.CASCADE)
    lat = models.FloatField(blank=True)
    lon = models.FloatField(blank=True)
    appeared_at = models.DateTimeField(null=True)
    disappeared_at = models.DateTimeField(null=True)


    def __str__(self):
        return f'lat: {self.lat}, lon: {self.lon}'




