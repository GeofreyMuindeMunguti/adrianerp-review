from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from .api import IssuesViewSet
from .monitoring import *
from .scorecard import *
# from django.urls import path, include
from django.conf.urls import url, include


router = routers.DefaultRouter()
router.register('api/issues',IssuesViewSet,'issues')



urlpatterns = [
      url('', include(router.urls)),
      #monotoring
      url('mile-stone-status/', MileStoneStatus.as_view()),
      url('budget-status/', BudgetStatus.as_view()),
      #scorecard
      url('site-rework-status/', SiteRework.as_view()),
]

