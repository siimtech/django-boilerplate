from django.contrib import admin
from .models import *
from unfold.admin import ModelAdmin
from django.contrib.auth.models import Group
from unfold.contrib.filters .admin import (
    RangeDateFilter,
)
from .forms import AppUserForm, AdminUserForm
from unfold.forms import AdminPasswordChangeForm, UserChangeForm, UserCreationForm


@admin.register(Admin)
class AdminUserAdmin(ModelAdmin):
    list_display = ['id', 'username', 'is_superuser', 'is_staff', 'email', 'is_active']
    form = AdminUserForm

    def has_delete_permission(self, request, obj=None):
        return False

@admin.register(AppUser)
class AppUserAdmin(ModelAdmin):
    list_display = ['id', 'username', 'phone_number', 'email', 'is_active', 'registered_at', 'last_login']
    list_filter = [
        ('registered_at', RangeDateFilter),
    ]
    form = AppUserForm
    

@admin.register(SocialAccount)
class SocialAccountAdmin(ModelAdmin):
    list_display = ['id', 'user', 'provider', 'uid']
    pass

admin.site.unregister(Group)
@admin.register(Group)
class GroupAdmin(ModelAdmin):
    list_display = ['name']
    list_display_links = ['name']
    search_fields = ['name']
