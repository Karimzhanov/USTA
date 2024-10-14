from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Настраиваем Swagger документацию
schema_view = get_schema_view(
    openapi.Info(
        title="API Documentation",
        default_version='v1',
        description="API documentation for the project",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@yourdomain.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

# Основные URL маршруты проекта
urlpatterns = [
    path('swagger.<str:format>', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

urlpatterns = [ 
    path('admin/', admin.site.urls),
    path('api/base/', include('apps.base.urls')),
    path('api/events/', include('apps.events.urls')),
    path('api/about_the_community/', include('apps.about_the_community.urls')),
    path('api/membership/', include('apps.membership.urls')),
    path('api/educert/', include('apps.educert.urls')),
    path('api/service/', include('apps.service.urls')),
    path('api/ambassadorship/', include('apps.ambassadorship.urls')),
    path('api/collaboration/', include('apps.collaboration.urls')),

]
