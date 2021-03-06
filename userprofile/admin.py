from __future__ import absolute_import

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from django.contrib.auth.models import User
from .models import UserProfile

admin.site.unregister(User)

class UserProfileInline(admin.StackedInline):
    model = UserProfile

class CustomUserAdmin(UserAdmin):
    list_display = ('email', 'username', 'is_superuser')
    list_filter = ('is_superuser',)

    # Not standard on model admin instances
    # The userAdmin class uses this to control which fields are shown in the add form.
    add_fieldsets = (
        (None, {
                'classes': ('wide',),
                'fields': {'email', 'username'}
               }),
    )
#    u = User.objects.get(pk=1) # Get the first user in the system.
#    user_cheese = u.get_profile().likes_cheese
    fieldsets = (
        (None, {'fields': (
                    'email', 'username', 'is_superuser', 'is_active'
        )}),
        ('Groups', {'fields': ('groups',)})
    )

    # Displays the fields handled by userprofile.
    inlines = [ UserProfileInline, ]

    search_fields = ('email', 'username')
    ordering = ('email',)
    filter_horizontal = ('groups',)

admin.site.register(User, CustomUserAdmin)
