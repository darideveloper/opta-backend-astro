from django.contrib.auth.models import User, Group
from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender=User)
def add_user_to_app_groups(sender, instance, created, **kwargs):
    if created:  # Only when user is first created
        app_groups = Group.objects.filter(name__icontains="app")
        instance.groups.add(*app_groups)