from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register('', MenuItemViewSet)


urlpatterns = [
]



urlpatterns += router.urls