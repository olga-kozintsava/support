from rest_framework import routers
from rest_framework.routers import DefaultRouter

from message.views import MessageViewSet

router = DefaultRouter()
router.register('messages', MessageViewSet, basename='message')
urlpatterns = router.urls
