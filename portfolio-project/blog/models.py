from django.db import models


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=80)
    published_at = models.DateTimeField()
    body = models.TextField(max_length=400)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]

    def published_at_pretty(self):
        return self.published_at.strftime('%b %e %Y')