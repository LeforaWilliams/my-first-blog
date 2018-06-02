from django.db import models

# Create your models here.

#here we are importins models and timezones from the django database
from django.db import models
from django.utils import timezone

#with class it is defining a model, post is the name of out model (should always start with uppercase),models.Model lets Django now that it is a django model
class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title