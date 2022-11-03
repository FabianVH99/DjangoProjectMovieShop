from platform import platform
from django.db import models
from django.utils.translation import gettext_lazy as _
import datetime

YEAR_CHOICES = []
for r in range(1900, (datetime.datetime.now().year+1)):
    YEAR_CHOICES.append((r,r))

class Movie(models.Model):

    class Genre(models.TextChoices):
        HORROR = _('Horror')
        ACTION =  _('Action')
        ADVENTURE =  _('Adventure')
        ROMANCE =  _('Romance')
        DISASTER =  _('Disaster')
        THRILLER =  _('Thriller')
        MUSICAL = _('Musical')
        COMEDY =  _('Comedy')
        DRAMA =  _('Drama')
        ANIMATION =  _('Animation')
        FAMILY = _('Family')
    
    class Platform(models.TextChoices):
        VHS = _('VHS')
        DVD = _('DVD')
        BLURAY = _('Blu-ray')

    title = models.CharField(max_length=200)
    description = models.TextField()
    genre = models.CharField(
        max_length=500,
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