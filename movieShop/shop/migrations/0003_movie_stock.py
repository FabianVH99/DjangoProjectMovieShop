# Generated by Django 4.1.2 on 2022-11-03 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_movie_platform_movie_release_alter_movie_genre'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='stock',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]
