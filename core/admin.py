# admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin
from django.contrib.auth.models import User, Group


class CustomUserAdmin(DefaultUserAdmin):
    
    def get_queryset(self, request):
        """ Return only app users for non-superusers """
        
        user = request.user

        # Get groups of the same user app
        if not user.is_superuser:
            user_groups = user.groups.all()
            user_group = user_groups.first().name if user_groups else None
            user_app = user_group.split(" ")[0] if user_group else None
            app_groups = Group.objects.filter(name__startswith=user_app)
            print(app_groups)

            # Get all users in the same app groups
            app_users = (
                super(DefaultUserAdmin, self)
                .get_queryset(request)  # Pass the 'request' argument here
                .filter(groups__in=app_groups)
            )
            print(app_users)

            return app_users

        return super().get_queryset(request)  # Pass the 'request' argument here


# Unregister the default User admin
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
