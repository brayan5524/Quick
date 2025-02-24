from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register('', UserViewSet)


urlpatterns = [
]



urlpatterns += router.urls