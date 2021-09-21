from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from ticket.models import Ticket
from ticket.permissions import IsAdminOrPostOnly, IsOwner
from ticket.serializers import TicketSerializer, UserTicketSerializer


class TicketViewSet(ModelViewSet):
    queryset = Ticket.objects.all()
    permission_classes = [IsAuthenticated, IsAdminOrPostOnly]

    def create(self, request, *args, **kwargs):
        new_ticket = Ticket.objects.create(text=request.data['text'], author=request.user)
        new_ticket.save()
        serializer = UserTicketSerializer(new_ticket)
        return Response(serializer.data)

    def get_serializer_class(self):
        if self.request.method == 'POST':
            serializer_class = UserTicketSerializer
        else:
            serializer_class = TicketSerializer
        return serializer_class

    def get_permissions(self):
        if self.action == 'retrieve':
            self.permission_classes = [IsOwner]
        return super().get_permissions()
