from django.contrib import admin

from . import models

# Register your models here.
admin.site.register(models.CollaboratingOrganization)
admin.site.register(models.EducationalProject)
admin.site.register(models.Event)
admin.site.register(models.Employer)
admin.site.register(models.IndustrialProject)
admin.site.register(models.Sponsor)
admin.site.register(models.Startup)
admin.site.register(models.News)
admin.site.register(models.Order)
admin.site.register(models.UserProfile)