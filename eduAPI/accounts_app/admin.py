from django.contrib import admin
from .models import User


class userAdmin(admin.ModelAdmin):
    list_display = ['id','first_name','email']

admin.site.register(User,userAdmin)