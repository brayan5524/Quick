from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register('', RestaurantViewSet)


urlpatterns = [
]



urlpatterns += router.urls