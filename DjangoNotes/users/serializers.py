from rest_framework import serializers
from models import User, Token
import logging

class TokenSerializer(serializers.BaseSerializer):
    class Meta:
        model = Token
        fields = ('token', 'duration')

class UserSerializer(serializers.BaseSerializer):
    class Meta:
        model = User
        fields = ('username', 'date', 'pwd', 'urlPhoto')
    
    def to_representation(self, obj):
        if type(obj) is User: 
            return {
                'username': obj.username,
                'date': obj.date, 
                'urlPhoto': obj.urlPhoto, 
                'pwd' : obj.pwd
            }
        else:
            return {
                'username': obj['username'],
                'date': obj['date'], 
                'urlPhoto': obj['urlPhoto'], 
                'pwd' : obj['pwd']
            }

    def to_internal_value(self, validated_data):
        logging.debug('create user')
        user = User(
            username=validated_data.get('username'),
            urlPhoto=validated_data.get('urlPhoto'),
            password=validated_data.get('pwd')
        )
        return user