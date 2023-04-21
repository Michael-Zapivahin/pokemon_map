from django.db import models


class Pokemon(models.Model):
    title_rus = models.CharField(max_length=200, verbose_name='название рус.')
    title_en = models.CharField(max_length=200, blank=True, verbose_name='название анл.')
    title_jp = models.CharField(max_length=200, blank=True, verbose_name='название япн.')
    description = models.TextField(blank=True, verbose_name='описание')
    image = models.ImageField(verbose_name='изображение')
    parent = models.ForeignKey(
        'self', on_delete=models.SET_NULL,
        null=True, blank=True, related_name='kids', verbose_name='Родитель'
    )

    def __str__(self):
        return self.title_en


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(
        Pokemon, on_delete=models.CASCADE, verbose_name='Свойства покемона', related_name='entities'
    )
    lat = models.FloatField(verbose_name='широта', blank=True, null=True)
    lon = models.FloatField(verbose_name='долгота', blank=True, null=True)
    appeared_at = models.DateTimeField(verbose_name='появился в', null=True, blank=True)
    disappeared_at = models.DateTimeField(verbose_name='исчез в', null=True, blank=True)
    level = models.IntegerField(verbose_name='уровень', null=True, blank=True)
    health = models.IntegerField(verbose_name='здоровье', null=True, blank=True)
    strength = models.IntegerField(verbose_name='атака', null=True, blank=True)
    defence = models.IntegerField(verbose_name='защита', null=True, blank=True)
    stamina = models.IntegerField(verbose_name='выносливость', null=True, blank=True)

    def __str__(self):
        return f'lat: {self.lat}, lon: {self.lon}'

