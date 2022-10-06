from django.contrib import admin

from .models import *


class ArticleAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


class SneakerAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("sneaker",)}


admin.site.register(Sneaker, SneakerAdmin)
admin.site.register(Brand)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Size)
admin.site.register(Feedback)
