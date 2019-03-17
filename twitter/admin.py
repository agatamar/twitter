from django.contrib import admin

from twitter import models

# Register your models here.
admin.site.register(models.Tweet)
admin.site.register(models.Comment)