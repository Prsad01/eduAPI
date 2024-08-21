from django.contrib import admin
from django.urls import path,include

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="My API",
        default_version='v1',
        description="My API description",
        terms_of_service="https://www.example.com/terms/",
        contact=openapi.Contact(email="contact@example.com"),
        license=openapi.License(name="Awesome License"),
    ),
    public=True,
    #permission_classes=(permissions.AllowAny),
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/',include('accounts_app.urls')),
    path('courses/',include('courses_app.urls')),
    path('api/',include('Lesson_app.urls')),
    path('enrollment/', include('enrollment_app.urls')),
    path('assignment/',include('assignment_app.urls')),
    path('submission/',include('submission_app.urls')),
    path('review/',include('review_app.urls')),
    

    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
