from django.urls import path, include
from rest_framework import routers
from users import views

router = routers.DefaultRouter()
router.register(r"appusers", views.AppUsersViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("register/", views.register, name="회원가입"),
]
