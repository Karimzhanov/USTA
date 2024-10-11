from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AboutViewSet, CommunityImageViewSet

router = DefaultRouter()
router.register(r'about', AboutViewSet, basename='about')
router.register(r'community-images', CommunityImageViewSet, basename='communityimage')

urlpatterns = [
    path('', include(router.urls)),
]
