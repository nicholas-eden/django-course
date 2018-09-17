from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=80)
    published_at = models.DateTimeField()
    body = models.TextField(max_length=400)
    url = models.TextField(max_length=400)
    image = models.ImageField(upload_to='images/')
    icon = models.ImageField(upload_to='images/')
    votes_total = models.IntegerField(default=1)
    hunter = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]

    def published_at_pretty(self):
        return self.published_at.strftime('%b %e %Y')

