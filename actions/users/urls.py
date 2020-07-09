from rest_framework import routers
from .views import BranchManagerList, ClientList
from django.urls import path

users_router = routers.DefaultRouter()

urlpatterns = [
    path("branch_managers/", BranchManagerList.as_view(), name="branch-managers"),
    path("clients/", ClientList.as_view(), name="clients"),
]
