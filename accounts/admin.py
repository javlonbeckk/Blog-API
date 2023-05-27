from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

#local imports
from .forms import CustomUserCreationForm, CustonUserChangeForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustonUserChangeForm
    model = CustomUser
    list_display = [
        "email",
        "username",
        "name",
        "is_staff",
    ]
    fieldsets = UserAdmin.fieldsets + ((None, {"fields": ("name", )}), )
    add_fieldsets = UserAdmin.add_fieldsets + ((None, {"fields": ("name", )}), )

admin.site.register(CustomUser, CustomUserAdmin)

