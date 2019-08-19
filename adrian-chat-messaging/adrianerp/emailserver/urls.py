from django.contrib.auth.views import LogoutView
from django.conf.urls import url, include
from . import views
from rest_framework import routers
from emailserver.views import EmailConfigViewSet


router = routers.DefaultRouter()
router.register(r'emailserver', EmailConfigViewSet)

urlpatterns = [
    url(r'^', include(router.urls)), 
]
 