import django_filters
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication

# Create your views here.
from rest_framework.permissions import IsAuthenticated

from chuku.models import Chuku
from chuku.serializers import UserChukuSerializer


class UserChukuViewSet(viewsets.ModelViewSet):
    queryset = Chuku.objects.all()
    serializer_class = UserChukuSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['product_name', 'logistic_code']

    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user).order_by('-updatedtime')

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user, status='created')
