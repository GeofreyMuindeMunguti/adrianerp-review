from rest_framework import serializers
from reports.models import *


class IssueSerializer(serializers.ModelSerializer):
    class Meta:
        model= Issues
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at', 'is_active')

# class BtsSiteSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = BtsSite
#         fields = '__all__'
#         read_only_fields = ('created_at', 'updated_at', 'is_active')



        

        

