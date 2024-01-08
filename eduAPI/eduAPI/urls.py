from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/',include('accounts_app.urls')),
    path('courses/',include('courses_app.urls')),
    path('api/',include('Lesson_app.urls')),
    path('enrollment/', include('enrollment_app.urls')),
    path('assignment/',include('assignment_app.urls')),
    path('submission/',include('submission_app.urls')),
    path('review/',include('review_app.urls')),
    
]
