from django.contrib import admin
from. import models

admin.site.register(models.User)
admin.site.register(models.Project)
admin.site.register(models.Subscription)
admin.site.register(models.RewardHistory)
# Register your models here.
