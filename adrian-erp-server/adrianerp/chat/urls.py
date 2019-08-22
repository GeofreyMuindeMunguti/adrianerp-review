from django.contrib.auth.views import LogoutView
from django.conf.urls import url, include
from . import views
from rest_framework import routers
from chat.views import ChatViewSet


router = routers.DefaultRouter()
router.register(r'chat', ChatViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
   
]
 