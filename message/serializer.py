from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from message.models import Message


class MessageSerializer(ModelSerializer):
    author = SerializerMethodField()

    class Meta:
        model = Message
        fields = ('ticket', 'author', 'message', 'sent_at')

    def get_author(self, obj):
        return obj.author.username

    # def create(self, validated_data):
    #     validated_data['author'] = self.context['author']
    #     return super().create(validated_data)

