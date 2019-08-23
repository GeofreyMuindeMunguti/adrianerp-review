from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from .api import *
from .monitoring import *
from .scorecard import *
from django.urls import path, include


router = routers.DefaultRouter()
router.register('api/issues',IssuesViewSet,'issues')
router.register('api/budget',BudgetViewSet,'budget')


urlpatterns = [
      path('', include(router.urls)),
      #monotoring
      path('mile-stone-status/', MileStoneStatus.as_view()),
      #scorecard
      path('site-rework-status/', SiteRework.as_view()),
]

