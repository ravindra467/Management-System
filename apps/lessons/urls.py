from django.urls import path, include
from rest_framework import routers
from .views import lessonsViewSet

router = routers.DefaultRouter()
router.register(r"", lessonsViewSet)

urlpatterns = [
    path("", include(router.urls)),
]