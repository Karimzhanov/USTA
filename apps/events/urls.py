from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.events.views import EventsViewSet, EventssViewSet, AnnouncementViewSet, AnnualEventViewSet,  VideoContentViewSet,  VideoContentsViewSet

router = DefaultRouter()
router.register(r'events', EventsViewSet)
router.register(r'eventss', EventssViewSet)
router.register(r'announcements', AnnouncementViewSet)
router.register(r'annual-events', AnnualEventViewSet)
router.register(r'video-content', VideoContentViewSet)
router.register(r'video-contents', VideoContentsViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
