from django.contrib import admin
from .models import ShortURL

# Register your models here.

class ShortURLModelAdmin(admin.ModelAdmin):

    list_display =  ['url' , 'timestamp' , 'updated']
    list_filter = ['url', 'timestamp' , 'updated']

    class Meta:
        model = ShortURL

admin.site.register(ShortURL,ShortURLModelAdmin)
