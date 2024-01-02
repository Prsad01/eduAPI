from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import UserView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter(trailing_slash=False)

router.register('user',UserView,basename='user')

urlpatterns = [
    path('api/token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
]+router.urls
