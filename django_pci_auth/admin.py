from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django_pci_auth.models import UserProfile, PasswordLog

from django.contrib.auth import get_user_model
User = get_user_model()

# https://docs.djangoproject.com/en/dev/topics/auth/\
# #storing-additional-information-about-users
# Define an inline admin descriptor for UserProfile model
# which acts a bit like a singleton
class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'profile'


# Define a new User admin
class UserAdmin(UserAdmin):
    inlines = (UserProfileInline, )


class PasswordLogAdmin(admin.ModelAdmin):
    list_display = ('user', 'password', 'create_date')
    list_filter = ['user', 'create_date']
    search_fields = ['user', 'create_date']
    date_hierarchy = 'create_date'


admin.site.unregister(User)  # Re-register UserAdmin
admin.site.register(User, UserAdmin)
admin.site.register(PasswordLog, PasswordLogAdmin)
