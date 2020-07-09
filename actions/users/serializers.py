from .models import BranchManager, Client, MedicalRecord, Score, Trainer
from rest_framework import serializers
from stock.serializers import BranchSerializer


class BranchManagerSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(source="user.first_name")
    last_name = serializers.CharField(source="user.last_name")

    class Meta:
        model = BranchManager
        fields = ("id", "first_name", "last_name", "branch")


class ClientSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(source="user.first_name")
    last_name = serializers.CharField(source="user.last_name")
    medical_record = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Client
        fields = (
            "id",
            "first_name",
            "last_name",
            "birth_date",
            "dni",
            "gender",
            "profile_picture",
            "phone",
            "address",
            "is_active",
            "client_since",
            "client_until",
            "routines",
            "medical_record",
        )
