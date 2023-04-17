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
    level = models.IntegerField(verbose_name='Level', null=True)
    health = models.IntegerField(verbose_name='Health', null=True)
    strength = models.IntegerField(verbose_name='Strength', null=True)
    defence = models.IntegerField(verbose_name='Defence', null=True)
    stamina = models.IntegerField(verbose_name='Stamina', null=True)

    def __str__(self):
        return f'lat: {self.lat}, lon: {self.lon}'

