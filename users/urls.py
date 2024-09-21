from django.urls import path, include
from rest_framework import routers
from users import views
from .views import CustomTokenObtainPairView
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

router = routers.DefaultRouter()
router.register(r"appusers", views.AppUsersViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("register/", views.register, name="users-register"),
    path("login/", CustomTokenObtainPairView.as_view(), name="users-login"),
    path("login/refresh/", TokenRefreshView.as_view(), name="users-token-refresh"),
]
