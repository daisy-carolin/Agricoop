from django.urls import include,path
from .views import UserDetailAPI,RegisterUserAPIView
from rest_framework import routers
from.views import RegisterUserAPIView


router=routers.SimpleRouter()
router.register(r"user",RegisterUserAPIView)

urlpatterns = [
  path("get-details",UserDetailAPI.as_view()),
  path("auth/user/registration",RegisterUserAPIView.as_view()),
]