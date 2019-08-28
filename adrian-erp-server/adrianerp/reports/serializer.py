from rest_framework import serializers
from .models import *
from logs.models import Log
from django.db.models.signals import post_save
from django.dispatch import receiver


class IssueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Issues
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at', 'is_active')


class BudgetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Budget
        fields = '__all__'

    @receiver(post_save,sender=Budget)
    def create_audit(instance, **kwargs):
         newlog = Log(user="Admin", action="budget/create")
         newlog.save()

      
