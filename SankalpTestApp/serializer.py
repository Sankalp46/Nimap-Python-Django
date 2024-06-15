from rest_framework import serializers
from .models import User,Client,Project

class ClientSerializer(serializers.ModelSerializer):
    created_by = serializers.ReadOnlyField(source='created_by.username')
    updated_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Client
        fields = ('id', 'client_name', 'created_at', 'created_by', 'updated_at')

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        formatted_representation = {
            'id': representation['id'],
            'client_name': representation['client_name'],
            'created_at': representation['created_at'],
            'created_by': representation['created_by'],
            'updated_at': representation['updated_at']
        }
        return formatted_representation

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = "__all__"

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['client'] = instance.client.client_name
        representation['users'] = [
            {'id': user.id, 'username': user.username}
            for user in instance.users.all()
        ]
        return representation