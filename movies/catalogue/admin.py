from django.contrib import admin
from models import Photo


class PhotoAdmin(admin.ModelAdmin):
    list_display = ("title", "uploaded", "admin_image")


admin.site.register(Photo, PhotoAdmin)
