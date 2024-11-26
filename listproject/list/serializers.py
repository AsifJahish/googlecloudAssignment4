from rest_framework import serializers
from .models import ListItem


class ListItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListItem
        fields = ['id', 'title', 'description', 'created_at', 'completed']