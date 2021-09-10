from django.contrib import admin
from .models import  Booking, Contact, Album, Artist



admin.site.register(Booking)
class  BookingAdmin(admin.ModelAdmin):
    list_filter = ['created_at','contacted']
    readonly_fields = ['created_at','contact','album','contacted']
    def has_add_permission(self,request):
       return False

class  BookingInline(admin.TabularInline):
    model = Booking
    fieldsets = [
        (None, {'fields':['album','contacted','created_at']})
    ]
    readonly_fields = ['created_at','album','contacted']
    extra = 0
    verbose_name = "Réservation"
    verbose_name_plural = "Réservations"

    def has_add_permission(self, request):
        return False


@admin.register(Contact)

class Contactadmin(admin.ModelAdmin):
        inlines = [BookingInline,]


class AlbumArtistsInline(admin.TabularInline):
    model = Album.artists.through
    extra = 1
    verbose_name = "Disque"
    verbose_name_plural = "Disques"

@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    search_fields = ['reference', 'title']

@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
     inlines = [AlbumArtistsInline,]


