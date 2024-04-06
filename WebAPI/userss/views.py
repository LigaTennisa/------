from django.contrib.auth.models import Group, User
from rest_framework import permissions, viewsets #Django REST Framework позволяет объединить логику для набора связанных представлений в одном классе, называемом a ViewSet

from .models import User
from userss.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
