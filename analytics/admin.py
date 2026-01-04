from django.contrib import admin
from .models import Artist, Track


@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ('name', 'spotify_id', 'popularity')
    search_fields = ('name', 'spotify_id')


@admin.register(Track)
class TrackAdmin(admin.ModelAdmin):
    list_display = ('name', 'artist', 'popularity')
    search_fields = ('name', 'spotify_id')
    list_filter = ('artist',)

from .models import ListeningSnapshot, SnapshotTrack

@admin.register(ListeningSnapshot)
class ListeningSnapshotAdmin(admin.ModelAdmin):
    list_display = ('user', 'period', 'created_at')
    list_filter = ('period', 'created_at')
    search_fields = ('user__username',)


@admin.register(SnapshotTrack)
class SnapshotTrackAdmin(admin.ModelAdmin):
    list_display = ('snapshot', 'track', 'position')
    list_filter = ('snapshot__period',)
