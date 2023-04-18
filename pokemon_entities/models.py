from django.db import models


class Pokemon(models.Model):
    title = models.TextField()
    title_en = models.CharField(max_length=200, blank=True, verbose_name='название анл.')
    title_jp = models.CharField(max_length=200, blank=True, verbose_name='название япн.')
    description = models.TextField(null=True)
    image = models.ImageField(blank=True)
    parent = models.ForeignKey(
        'self', on_delete=models.SET_NULL, null=True, blank=True, related_name='kids', verbose_name='эволюция'
    )

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

