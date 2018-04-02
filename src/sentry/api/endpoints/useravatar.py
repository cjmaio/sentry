from __future__ import absolute_import

from rest_framework import status
from rest_framework.response import Response

from sentry.api.bases.avatar import AvatarMixin
from sentry.api.bases.user import UserEndpoint
from sentry.models import UserAvatar


class UserAvatarEndpoint(AvatarMixin, UserEndpoint):
    object_type = 'user'
    model = UserAvatar

    def get(self, request, user):
        return super(UserAvatarEndpoint, self).get(request, user)

    def put(self, request, user):
        if user != request.user:
            return Response(status=status.HTTP_403_FORBIDDEN)

        return super(UserAvatarEndpoint, self).put(request, user)
