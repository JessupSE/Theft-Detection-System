from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AlertViewSet, MediaFileViewSet, KnownPersonViewSet

router = DefaultRouter()
router.register(r'alerts', AlertViewSet)
router.register(r'media', MediaFileViewSet)
router.register(r'known-persons', KnownPersonViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
