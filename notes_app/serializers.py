from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Note

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ['id', 'content', 'created_at', 'updated_at', 'owner']
        read_only_fields = ['owner']

class NoteShareSerializer(serializers.Serializer):
    shared_with = serializers.ListField(child=serializers.EmailField())

class NoteUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ['content']

class NoteVersionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ['note', 'content', 'edited_by', 'created_at']
