from .serializers import BranchManagerSerializer, ClientSerializer
from rest_framework.generics import ListCreateAPIView
from .models import BranchManager, Client
from rest_framework.permissions import IsAdminUser


class BranchManagerList(ListCreateAPIView):
    queryset = BranchManager.objects.all()
    serializer_class = BranchManagerSerializer
    permission_classes = [IsAdminUser]


class ClientList(ListCreateAPIView):
    queryset = Client.objects.filter(is_active=True)
    serializer_class = ClientSerializer
    permission_classes = [IsAdminUser]
