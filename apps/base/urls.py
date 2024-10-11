from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.base.views import PageContentViewSet, ContentBlockViewSet, PartnerViewSet, EventViewSet, EventImageViewSet, ProjectParticipationViewSet, ProjectImageViewSet, TeamMemberViewSet, ContentBlocksViewSet


router = DefaultRouter()
router.register(r'page-content', PageContentViewSet)
router.register(r'content-blocks', ContentBlockViewSet)
router.register(r'partners', PartnerViewSet)
router.register(r'events', EventViewSet)
router.register(r'event-images', EventImageViewSet)
router.register(r'project-participation', ProjectParticipationViewSet)
router.register(r'project-images', ProjectImageViewSet)
router.register(r'team-members', TeamMemberViewSet)
router.register(r'content-blocks-categories', ContentBlocksViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
