from django.contrib import admin

from .models import UserData

# Register your models here.


@admin.register(UserData)
class UserDataAdmin(admin.ModelAdmin):
    list_display = ['username' , 'email' , 'password']

