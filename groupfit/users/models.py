from django.db import models
from django.contrib.auth.models import User
from groups.models import WorkoutGroup
from django.db.models.signals import post_save
from django.core.urlresolvers import reverse
from tags.models import Tag
from playlists.models import Playlist


class UserProfile( models.Model ):
    """
    This UserProfile model wraps the default Django auth User model with
    additional information, including their groups, playlists, tags
    (interests), etc.
    """

    user = models.OneToOneField(
        User,
    )

    groups = models.ManyToManyField(
        WorkoutGroup,
        blank = True,
        related_name = "members",
    )

    tags = models.ManyToManyField(
        Tag,
        blank = True,
    )

    playlists = models.ManyToManyField(
        Playlist,
        blank = True,
    )

    def __unicode__(self):
        return "%s" % self.user.username

    def get_absolute_url(self):
        return reverse('users.views.view_user', args=[str(self.pk)])


"""
This post_save function is triggered when a User object is created,
creating a UserProfile object along with it.
"""
def create_user_profile( sender, instance, created, **kwargs ):
    if created:
        UserProfile.objects.create(user=instance)
#post_save.connect(create_user_profile, sender=User)
