from rest_framework import serializers
from ticket.models import Ticket


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ('id', 'author', 'status', 'text')

    def create(self, validated_data):
        return Ticket.objects.create(**validated_data)

