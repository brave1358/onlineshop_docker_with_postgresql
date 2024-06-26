from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    form = CustomUserCreationForm
    add_form = CustomUserChangeForm
    list_display = ('email', 'username',)
