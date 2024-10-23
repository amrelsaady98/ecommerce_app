
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from authentication.models import User

class MyUserAdmin(UserAdmin):
    # Define the fields to be displayed in the list view
    list_display = ('email', 'first_name', 'last_name', 'is_staff')

    # Add fields for searching
    search_fields = ('email', 'first_name', 'last_name')

    # Define the fieldsets to organize the fields on the detail page
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (('Personal info'), {'fields': ('first_name', 'last_name')}),
        (('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                        'groups', 'user_permissions')}),
        (('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )

    # Define the add form layout for creating a new user
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'last_name', 'date_of_birth', 'password1', 'password2'),
        }),
    )

    # Specify the fields for ordering users in the admin list
    ordering = ('email',)

    # Define which fields should appear as filters in the list view
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')

admin.site.register(User, MyUserAdmin)
# Register your models here.

