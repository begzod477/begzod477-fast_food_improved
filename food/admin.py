from django.contrib import admin
from .models import Category, Food, Like, Comment

# Register your models here.

admin.site.register(Category)
admin.site.register(Food)
admin.site.register(Like)
admin.site.register(Comment)

