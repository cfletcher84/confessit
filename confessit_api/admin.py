from django.contrib import admin
from confessit_api import models

admin.site.register(models.UserProfile)
admin.site.register(models.ProfileFeedItem)
