from django.contrib import admin

from Insta.models import InstaUser, Like, Post

# Register your models here.
admin.site.register(Post)
admin.site.register(InstaUser)
admin.site.register(Like)