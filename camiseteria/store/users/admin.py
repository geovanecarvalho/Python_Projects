from django.contrib import admin
# Register your models here.
from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from .models import User
from .forms import UserChangeForm, UserCreationForm

@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    model = User
    fieldsets = auth_admin.UserAdmin.fieldsets + (
        ("Campos Personalizados", {"fields": ("data", )}),
    )