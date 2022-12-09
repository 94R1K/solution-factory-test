from django.urls import re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title='Сервис уведомлений API',
        default_version='v1',
        description='Документация для сервиса уведомлений.',
        terms_of_service='https://yandex.ru/legal/confidential/',
        contact=openapi.Contact(email='real-man228@yandex.ru'),
        license=openapi.License(name='BSD License'),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

swaggerurlpatterns = [
   re_path(
       r'^docs/$',
       schema_view.with_ui('swagger', cache_timeout=0),
       name='schema-swagger-ui'
   ),
]
