from rest_framework import serializers, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from message.models import Message
from message.serializer import MessageSerializer
from ticket.models import Ticket
from ticket.permissions import IsAdminOrPostOnly, IsOwner
from ticket.serializers import TicketSerializer, UserTicketSerializer


class TicketViewSet(ModelViewSet):
    queryset = Ticket.objects.all().prefetch_related('messages')
    permission_classes = [IsAuthenticated, IsAdminOrPostOnly]

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['author'] = self.request.user
        return context

    def get_serializer_class(self):
        if self.request.method == 'POST':
            serializer_class = UserTicketSerializer
        else:
            serializer_class = TicketSerializer
        return serializer_class

    @action(detail=True, methods=['GET', 'POST'], permission_classes=[IsOwner])
    def messages(self, request, pk=None):
        if request.method == 'GET':
            queryset = Message.objects.filter(ticket_id=pk)
            serializer = MessageSerializer(queryset, many=True)
            return Response(serializer.data)
        else:
            if 'message' in request.data:
                new_message = Message.objects.create(message=request.data['message'],
                                                     author=request.user,
                                                     ticket_id=pk)
                serializer = MessageSerializer(new_message)
                return Response(serializer.data)
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def get_permissions(self):
        if self.action == 'retrieve':
            self.permission_classes = [IsOwner]
        return super().get_permissions()
