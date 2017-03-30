from django.db import models
from shortener.models import ShortURL
# Create your models here.


class ClickManager(models.Manager):

    def create_event(self,instance):
        if isinstance(instance, ShortURL):
            obj, created = self.get_or_create(shortUrl=instance)
            if not created:
                obj.count += 1
                obj.save()
                return obj.count
            return None

    def reset_all_counts(self):
        qs = self.all()
        for q in qs:
            q.count = 0
            q.save()
        return "All counts set to 0"

class Click(models.Model):
    shortUrl = models.OneToOneField(ShortURL,on_delete=models.CASCADE)
    count = models.IntegerField(default=0)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    objects = ClickManager()

    def __str__(self):
        return "{}".format(self.count)
