from rest_framework import serializers
from user.models import User, UserProfile
from django.contrib.auth import logout, login
from logs.models import Log

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('position', 'phone', 'team',  'profile_pic')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    
    profile = UserProfileSerializer(required=True)

    class Meta:
        model = User
        fields = ('url', 'email', 'first_name', 'last_name', 'password', 'profile')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        profile_data = validated_data.pop('profile')
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        UserProfile.objects.create(user=user, **profile_data)
      
        newlog = Log(user="Admin", action="user/create")
        newlog.save()

        return user

    def update(self, instance, validated_data):
        profile_data = validated_data.pop('profile')
        profile = instance.profile
        instance.email = validated_data.get('email', instance.email)
        instance.save()
        profile.position = profile_data.get('position', profile.position)
        profile.phone = profile_data.get('phone', profile.phone)
        profile.team = profile_data.get('team', profile.team)
        profile.profile_pic = profile_data.get('profile_pic', profile.profile_pic)
        profile.save()

        
        newlog = Log(user="Admin", action="user/update")
        newlog.save()


        return instance

    
    
