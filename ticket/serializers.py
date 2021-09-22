from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from message.serializer import MessageSerializer
from ticket.models import Ticket


class TicketSerializer(ModelSerializer):
    messages = MessageSerializer(many=True)

    class Meta:
        model = Ticket
        fields = ('id', 'author', 'status', 'task', 'messages')
        read_only_fields = ('id', 'author', 'task', 'messages')


class UserTicketSerializer(ModelSerializer):
    task = serializers.CharField(required=True)

    class Meta:
        model = Ticket
        fields = ('task',)

    def create(self, validated_data):
        validated_data['author'] = self.context['author']
        return super().create(validated_data)
