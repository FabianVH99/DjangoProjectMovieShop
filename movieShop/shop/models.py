from django.db import models
from django.utils.translation import gettext_lazy as _

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

    title = models.CharField(max_length=200)
    description = models.TextField()
    genre = models.CharField(
        max_length=2,
        choices=Genre.choices,
        default=Genre.HORROR,
    )
    price = models.DecimalField(max_digits=4, decimal_places=2)
    image = models.CharField(max_length=5000, null=True, blank=True)