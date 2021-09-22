from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from message.models import Message


class MessageSerializer(ModelSerializer):
    author = SerializerMethodField()

    class Meta:
        model = Message
        fields = ('ticket', 'author', 'message', 'sent_at')

    @staticmethod
    def get_author(obj):
        return obj.author.username

