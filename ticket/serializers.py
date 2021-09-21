from rest_framework import serializers
from ticket.models import Ticket


class TicketSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ticket
        fields = ('id', 'author', 'status', 'text')
        read_only_fields = ('id', 'author', 'text')


class UserTicketSerializer(serializers.ModelSerializer):
    text = serializers.CharField(required=True)

    class Meta:
        model = Ticket
        fields = ('text',)
