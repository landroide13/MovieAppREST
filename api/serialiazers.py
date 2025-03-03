from rest_framework import serializers
from rest_framework.authtoken.models import Token

from api.models import Movie, Rating
from django.contrib.auth.models import User

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('id', 'name', 'description')


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ('id', 'movie', 'user', 'stars')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username', 'password', 'email')
        extra_kwargs = {'password': { 'write_only': True , 'required': True }}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user    






