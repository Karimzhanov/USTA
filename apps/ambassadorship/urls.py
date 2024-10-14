from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.ambassadorship.views import AmbassadorshipViewSet, AmbassadorshipImageViewSet

router = DefaultRouter()
router.register(r'ambassadorships', AmbassadorshipViewSet, basename='ambassadorship')
router.register(r'ambassadorship-images', AmbassadorshipImageViewSet, basename='ambassadorship-image')

urlpatterns = [
    path('', include(router.urls)),
]
