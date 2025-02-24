from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'item', OrderItemViewSet)
router.register('', OrderViewSet)




urlpatterns = [
]


urlpatterns += router.urls