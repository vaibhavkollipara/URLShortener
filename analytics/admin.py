from django.contrib import admin
from .models import Click
# Register your models here.


class ClickModelAdmin(admin.ModelAdmin):
    list_display = ['shortUrl', 'count', 'timestamp','updated']

admin.site.register(Click,ClickModelAdmin)
