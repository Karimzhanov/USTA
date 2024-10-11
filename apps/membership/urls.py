from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MembershipViewSet, ContentBlockViewSet, CategoryViewSet, StepInstructionViewSet

router = DefaultRouter()
router.register(r'memberships', MembershipViewSet)
router.register(r'content-blocks', ContentBlockViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'step-instructions', StepInstructionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
