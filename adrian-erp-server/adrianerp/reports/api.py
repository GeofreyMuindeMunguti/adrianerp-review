from  .models import *
from rest_framework import viewsets,permissions
from .serializer import *


class IssuesViewSet(viewsets.ModelViewSet):
    queryset = Issues.objects.order_by('created_at')
    serializer_class = IssueSerializer

    search_fields = ('project_name', )
    ordering_fields = ('updated_at', 'project_name', )


class BudgetViewSet(viewsets.ModelViewSet):
        queryset = Budget.objects.all()
        serializer_class = BudgetSerializer

  
  