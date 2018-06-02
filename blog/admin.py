#here we import the post model we have created in the models file
from django.contrib import admin
from .models import Post
# Register your models here.
admin.site.register(Post)

#creating a superuser in the command line that has control over everything in the site
