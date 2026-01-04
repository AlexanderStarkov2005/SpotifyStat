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

from django.conf import settings

class ListeningSnapshot(models.Model):
    PERIOD_SHORT = 'short_term'
    PERIOD_MEDIUM = 'medium_term'
    PERIOD_LONG = 'long_term'

    PERIOD_CHOICES = (
        (PERIOD_SHORT, 'Last 4 weeks'),
        (PERIOD_MEDIUM, 'Last 6 months'),
        (PERIOD_LONG, 'All time'),
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='listening_snapshots'
    )
    period = models.CharField(
        max_length=20,
        choices=PERIOD_CHOICES
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.user.username} — {self.period} — {self.created_at:%Y-%m-%d}'

class SnapshotTrack(models.Model):
    snapshot = models.ForeignKey(
        ListeningSnapshot,
        on_delete=models.CASCADE,
        related_name='snapshot_tracks'
    )
    track = models.ForeignKey(
        Track,
        on_delete=models.CASCADE,
        related_name='track_snapshots'
    )
    position = models.PositiveIntegerField()

    class Meta:
        unique_together = ('snapshot', 'position')
        ordering = ('position',)

    def __str__(self) -> str:
        return f'{self.snapshot} — {self.track} ({self.position})'

