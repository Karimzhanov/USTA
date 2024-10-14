from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.collaboration.views import СollaborationViewSet, ProjectViewSet, ProjectsPageViewSet, AwardViewSet, MentoringProgramsViewSet

router = DefaultRouter()
router.register(r'collaboration', СollaborationViewSet)
router.register(r'projects', ProjectViewSet)
router.register(r'projects-page', ProjectsPageViewSet)
router.register(r'awards', AwardViewSet)
router.register(r'mentoring-programs', MentoringProgramsViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
