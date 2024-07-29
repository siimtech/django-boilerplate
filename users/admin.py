from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *
from unfold.admin import ModelAdmin
from django.contrib.auth.models import Group


@admin.register(Admin)
class AdminUserAdmin(ModelAdmin):
    pass

@admin.register(AppUser)
class AppUserAdmin(ModelAdmin):
    pass

@admin.register(SocialAccount)
class SocialAccountAdmin(ModelAdmin):
    pass

admin.site.unregister(Group)
@admin.register(Group)
class GroupAdmin(ModelAdmin):
    list_display = ['name']
    list_display_links = ['name']
    search_fields = ['name']

