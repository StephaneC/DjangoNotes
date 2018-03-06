from rest_framework import serializers
from models import User

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'date', 'photo')
    
    def to_representation(self, obj):
        return {
            'username': obj.username,
            'date': obj.date, 
            'urlPhoto': obj.urlPhoto
        }

    def to_internal_value(self, validated_data):
        logging.debug('create user')
        user = User(
            username=validated_data.get('username'),
            date=validated_data.get('date'),
            urlPhoto=validated_data.get('urlPhoto'),
            password=validated_data.get('password')
        )
        return note