# serializers.py
from rest_framework import serializers
from .models import Note

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ['id', 'title', 'content', 'created_on', 'last_update']
        read_only_fields = ['id', 'created_on', 'last_update']
