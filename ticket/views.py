from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from message.services import get_messages, post_message
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
            return UserTicketSerializer
        else:
            return TicketSerializer

    def get_permissions(self):
        if self.action == 'retrieve':
            self.permission_classes = [IsOwner]
        return super().get_permissions()

    @action(detail=True, methods=['GET', 'POST'], permission_classes=[IsOwner])
    def messages(self, request, pk=None):
        # need to check permissions
        my_obj = self.get_object()
        if request.method == 'POST':
            return post_message(request, pk)
        else:
            return get_messages(pk)


