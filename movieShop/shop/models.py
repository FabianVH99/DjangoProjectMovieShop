from platform import platform
from django.db import models
from django.core.mail import send_mass_mail
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
        FANTASY = _('Fantasy')
        SCIFI = _('Sci-fi')
    
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
        max_length=500,
        choices=Platform.choices,
        default=Platform.BLURAY,
    )
    price = models.DecimalField(max_digits=4, decimal_places=2)
    stock = models.PositiveSmallIntegerField(default=0)
    sold = models.PositiveSmallIntegerField(default=0)
    image = models.CharField(max_length=5000, null=True, blank=True)
    scene1 = models.CharField(max_length=5000, null=True, blank=True)
    scene2 = models.CharField(max_length=5000, null=True, blank=True)
    scene3 = models.CharField(max_length=5000, null=True, blank=True)

    def save(self):
        if self.id:
            old_movie = Movie.objects.get(id=self.id)
            if old_movie.stock < 1 and self.stock > 0:
                recipient_list = Subscription.objects.filter(movie_id=self.id)
                stock_message = ('Stock updated for ' + self.title, 'The movie you are subscribed to is back in stock!', 'fabian.vanhaelen@student.odisee.be', recipient_list)
                send_mass_mail((stock_message), fail_silently=False)
        super(Movie, self).save()

class Subscription(models.Model):
    name = models.CharField(max_length=50)
    mail = models.EmailField(max_length=254)
    movie_id = models.PositiveSmallIntegerField(default=0)