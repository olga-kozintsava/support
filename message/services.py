from rest_framework import status
from rest_framework.response import Response

from message.models import Message
from message.serializer import MessageSerializer


def get_messages(pk):
    queryset = Message.objects.filter(ticket_id=pk)
    serializer = MessageSerializer(queryset, many=True)
    return Response(serializer.data)


def post_message(request, pk):
    if 'message' in request.data:
        new_message = Message.objects.create(message=request.data['message'],
                                             author=request.user,
                                             ticket_id=pk)
        serializer = MessageSerializer(new_message)
        return Response(serializer.data)
    return Response(status=status.HTTP_400_BAD_REQUEST)
