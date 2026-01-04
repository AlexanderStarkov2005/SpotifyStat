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
