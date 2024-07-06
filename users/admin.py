from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *



admin.site.register(AppUser)
admin.site.register(SocialAccount)
admin.site.register(Admin, UserAdmin)
