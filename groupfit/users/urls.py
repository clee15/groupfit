from django.conf.urls import patterns, include, url
from users.views import view_user

urlpatterns = patterns('',
    # Register
    url(r'^register', register),
    
    # Create a user profile.
    url(r'^create/$', create_user),

    # View a user profile.
    url(r'^(?P<user_pk>\d+)$', view_user),

)
