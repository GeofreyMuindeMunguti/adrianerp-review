from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from .api import *
from .monitoring import *
from .scorecard import *
from django.conf.urls import url, include


router = routers.DefaultRouter()
router.register('api/issues',IssuesViewSet,'issues')
router.register('api/budget',BudgetViewSet,'budget')


urlpatterns = [
      url('', include(router.urls)),
      #monotoring
      url('mile-stone-status/', MileStoneStatus.as_view()),
      #scorecard
      url('site-rework-status/', SiteRework.as_view()),
]

