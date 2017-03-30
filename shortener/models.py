from django.db import models
from .utils import create_shortcode
from django.conf import settings


SHORTCODE_MAX = getattr(settings, "SHORTCODE_MAX",15)

class ShortURLManager(models.Manager):

    def all(self,*args,**kwargs):
        qs_main = super(ShortURLManager,self).all(*args,**kwargs)
        qs = qs_main.filter(active=True)
        return qs

    def refresh_shorturls(self):
        qs = ShortURL.objects.filter(id__gte=1)
        new_codes = 0
        for q in qs:
            q.shorturl = None
            q.save()
            new_codes += 1
        return "refreshed {} urls".format(new_codes)


class ShortURL(models.Model):
    url = models.CharField(max_length=250)
    shorturl = models.CharField(max_length=SHORTCODE_MAX,
                                unique=True,
                                blank=True
                                )
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    objects = ShortURLManager()

    def save(self,*args,**kwargs):
        if self.shorturl is None or self.shorturl=='':
            self.shorturl = create_shortcode(self)
        super(ShortURL,self).save(*args,**kwargs)

    def __str__(self):
        return str(self.url)

    def __unicode__(self):
        return str(self.url)

    def get_shorturl(self):
        return