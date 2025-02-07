from django.urls import path
from config.urls import urlpatterns as main_urls
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Django Mini API",
      default_version='v1',
      description="장고 미니프로젝트 API 입니다.",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="eodyd426@gmail.com"),
      license=openapi.License(name="LDY License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
   path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
] + main_urls
