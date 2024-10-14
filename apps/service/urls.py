from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ServiceViewSet, ServiceImageViewSet, ArticleViewSet, ServicesViewSet

router = DefaultRouter()
router.register(r'services', ServiceViewSet, basename='service')
router.register(r'service-images', ServiceImageViewSet, basename='service-image')
router.register(r'articles', ArticleViewSet, basename='article')
router.register(r'services-list', ServicesViewSet, basename='services-list')

# URL-ы приложения
urlpatterns = [
    path('', include(router.urls)),
]
