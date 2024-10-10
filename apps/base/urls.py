from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.base.views import PageContentViewSet, ContentBlockViewSet, PartnerViewSet, EventViewSet, EventImageViewSet, ProjectParticipationViewSet,TeamMemberViewSet, AmbassadorViewSet,EducationViewSet,CommunitiesViewSet,MembershipViewSet,ServiceViewSet

router = DefaultRouter()
router.register(r'page-content', PageContentViewSet, basename='page-content')
router.register(r'content-blocks', ContentBlockViewSet, basename='content-blocks')
router.register(r'partners', PartnerViewSet, basename='partners')
router.register(r'events', EventViewSet, basename='events')
router.register(r'event-images', EventImageViewSet, basename='event-images')
router.register(r'projects', ProjectParticipationViewSet, basename='projects')
router.register(r'team-members', TeamMemberViewSet, basename='team-members')
router.register(r'ambossador', AmbassadorViewSet, basename='ambossador')
router.register(r'education', EducationViewSet, basename='education')
router.register(r'communities', CommunitiesViewSet, basename='communities')
router.register(r'membership', MembershipViewSet, basename='membership')
router.register(r'service', ServiceViewSet, basename='service')




urlpatterns = [
    path('', include(router.urls)), 
]



