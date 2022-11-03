from platform import platform
from django.db import models
from django.utils.translation import gettext_lazy as _
import datetime

YEAR_CHOICES = []
for r in range(1900, (datetime.datetime.now().year+1)):
    YEAR_CHOICES.append((r,r))

class Movie(models.Model):

    class Genre(models.TextChoices):
        HORROR = 'HR', _('Horror')
        ACTION = 'AC', _('Action')
        ADVENTURE = 'AD', _('Adventure')
        ROMANCE = 'RM', _('Romance')
        DISASTER = 'DS', _('Disaster')
        THRILLER = 'TH', _('Thriller')
        MUSICAL = 'MS', _('Musical')
        COMEDY = 'CM', _('Comedy')
        DRAMA = 'DR', _('Drama')
        ANIMATION = 'AN', _('Animation')
        FAMILY = 'FM', _('Family')
    
    class Platform(models.TextChoices):
        VHS = 'VH', _('VHS')
        DVD = 'DV', _('DVD')
        BLURAY = 'BR', _('Blu-ray')

    title = models.CharField(max_length=200)
    description = models.TextField()
    genre = models.CharField(
        max_length=2,
        choices=Genre.choices,
        default=Genre.HORROR,
    )
    release = models.IntegerField(_('year'), choices=YEAR_CHOICES, default=datetime.datetime.now().year)
    platform = models.CharField(
        max_length=2,
        choices=Platform.choices,
        default=Platform.BLURAY,
    )
    price = models.DecimalField(max_digits=4, decimal_places=2)
    stock = models.PositiveSmallIntegerField(default=0)
    image = models.CharField(max_length=5000, null=True, blank=True)