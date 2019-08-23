from rest_framework import serializers
from .models import *


class IssueSerializer(serializers.ModelSerializer):
    class Meta:
        model= Issues
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at', 'is_active')


class BudgetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Budget
        fields = '__all__'



        

        

