from rest_framework import generics, mixins
from rest_framework.viewsets import ModelViewSet, GenericViewSet

from message.models import Message
from message.serializer import MessageSerializer


# class MessageCreate(mixins.CreateModelMixin,
#                     GenericViewSet):
#

# queryset = Message.objects.all()
#     serializer_class = MessageSerializer
#
#     def get_serializer_context(self):
#         context = super().get_serializer_context()
#         context['author'] = self.request.user
#         return context


class MessageViewSet(ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['author'] = self.request.user
        return context
