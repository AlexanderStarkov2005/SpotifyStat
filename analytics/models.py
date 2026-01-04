from django.db import models


class Artist(models.Model):
    spotify_id = models.CharField(
        max_length=128,
        unique=True
    )
    name = models.CharField(max_length=255)
    genres = models.JSONField(
        null=True,
        blank=True
    )
    popularity = models.IntegerField(
        null=True,
        blank=True
    )

    def __str__(self) -> str:
        return self.name


class Track(models.Model):
    spotify_id = models.CharField(
        max_length=128,
        unique=True
    )
    name = models.CharField(max_length=255)
    artist = models.ForeignKey(
        Artist,
        on_delete=models.CASCADE,
        related_name='tracks'
    )
    popularity = models.IntegerField(
        null=True,
        blank=True
    )
    energy = models.FloatField(
        null=True,
        blank=True
    )
    danceability = models.FloatField(
        null=True,
        blank=True
    )
    tempo = models.FloatField(
        null=True,
        blank=True
    )

    def __str__(self) -> str:
        return f'{self.name} — {self.artist.name}'
