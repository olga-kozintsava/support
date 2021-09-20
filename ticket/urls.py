from rest_framework import routers
from rest_framework.routers import DefaultRouter

from ticket.views import TicketViewSet

router = DefaultRouter()
router.register('tickets', TicketViewSet, basename='ticket')
urlpatterns = router.urls
