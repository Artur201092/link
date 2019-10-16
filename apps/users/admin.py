from django.contrib import admin

from apps.users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'first_name',
        'last_name',
        'phone',
        'email',
        'is_active',
    ]

    search_fields = [
        'username',
        'first_name',
        'last_name',
        'phone',
        'email',
    ]

    class Meta:
        model = User