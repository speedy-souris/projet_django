from django.contrib import admin
from listings.models import Band
from listings.models import Article


class BandAdmin(admin.ModelAdmin):
    list_display = ('name', 'year_formed', 'genre')

admin.site.register(Band, BandAdmin)
admin.site.register(Article)
# Register your models here.
