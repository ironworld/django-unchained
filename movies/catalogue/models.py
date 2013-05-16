from django.db import models
from movies.settings import MEDIA_URL


class Photo(models.Model):
    image = models.ImageField(upload_to="covers")
    title = models.CharField(max_length=150)
    uploaded = models.DateField()

    def admin_image(self):
        return '<img src="%s%s" height="75"/>' % (MEDIA_URL, self.image)
    admin_image.allow_tags = True

    def __unicode__(self):
        return self.title
