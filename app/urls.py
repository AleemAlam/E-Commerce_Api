from django.urls import path, include
from rest_framework import routers
from .views import ItemViewSet, RatingViewSet

router = routers.DefaultRouter()
router.register('item', ItemViewSet)
router.register('ratings', RatingViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]