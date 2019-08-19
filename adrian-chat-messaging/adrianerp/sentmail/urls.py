from django.contrib.auth.views import LogoutView
from django.conf.urls import url, include
from . import views
from rest_framework import routers
from sentmail.views import SentEmailViewSet


router = routers.DefaultRouter()
router.register(r'email', SentEmailViewSet)

urlpatterns = [
    url(r'^', include(router.urls)), 
]
 