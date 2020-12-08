from django.db import models


class Pokemon(models.Model):
    title = models.CharField(verbose_name="Имя покемона", max_length=200)
    image = models.ImageField(verbose_name="Картинка", null=True)
    description = models.TextField(verbose_name="Описание", blank=True)
    title_en = models.CharField(verbose_name="Название на английском", max_length=200, blank=True)
    title_jp = models.CharField(verbose_name="Название на японском", max_length=200, blank=True)
    previous_evolution = models.ForeignKey("self",
                                           verbose_name='Из кого эволюционирует',
                                           null=True,
                                           blank=True,
                                           related_name='next_evolutions',
                                           on_delete=models.SET_NULL
                                           )



    def __str__(self):
        return "{}".format(self.title)


class PokemonEntity(models.Model):
    lat = models.FloatField(verbose_name="Ширина")
    lon = models.FloatField(verbose_name="Долгота")
    pokemon = models.ForeignKey(Pokemon, verbose_name="Покемон", on_delete=models.CASCADE)
    appeared_at = models.DateTimeField(verbose_name="Появится", null=True, blank=True)
    disappeared_at = models.DateTimeField(verbose_name="Исчезнет", null=True, blank=True)
    level = models.IntegerField(verbose_name="Уровень", null=True, blank=True)
    health = models.IntegerField(verbose_name="Здоровье", null=True, blank=True)
    strength = models.IntegerField(verbose_name="Сила", null=True, blank=True)
    defence = models.IntegerField(verbose_name="Защита", null=True, blank=True)
    stamina = models.IntegerField(verbose_name="Выносливость", null=True, blank=True)
