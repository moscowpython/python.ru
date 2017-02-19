from django.contrib import admin

from . import models


admin.site.register(models.Employer)
admin.site.register(models.Speaker)
admin.site.register(models.Talk)
