from django.contrib import admin
from ablog.models import User
from .models import Post, Category,Profile, Comment

admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Profile)
admin.site.register(Comment)

admin.site.register(User)

