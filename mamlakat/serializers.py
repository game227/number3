from .models import Mamlakat
from rest_framework import serializers

class MamlakatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mamlakat
        fields = ['id', 'name', 'plase', 'created_at', 'update_at']
        read_only_fields = ['id','created_at', 'update_at']