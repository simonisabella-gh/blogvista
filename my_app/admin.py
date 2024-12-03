from django.contrib import admin
from .models import userTable, Category, Post,Comment

admin.site.register(userTable)
admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Comment)


# Register your models here.
