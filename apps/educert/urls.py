from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.educert.views import EducertViewSet, ContentblockViewSet, VideooViewSet

router = DefaultRouter()

router.register(r'educert', EducertViewSet, basename='educert')
router.register(r'contentblocks', ContentblockViewSet, basename='contentblock')
router.register(r'videos', VideooViewSet, basename='videoo')

urlpatterns = [
    path('', include(router.urls)),
]
