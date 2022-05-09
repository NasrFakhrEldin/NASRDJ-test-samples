from django.contrib import admin
from .models import Pic


# Define the picadmin class

class PicAdmin(admin.ModelAdmin):
    exclude = ["picture","content_type"]


# Register your models here.

admin.site.register(Pic, PicAdmin)