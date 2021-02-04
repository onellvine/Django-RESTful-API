from rest_framework import serializers
from .models import SysUser, Movie, Comment


class RegisterUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = SysUser
        fields = ('username', 'phone', 'password')
        extra_kwargs ={'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)

        if password is not None:
            instance.set_password(password)
        instance.save()

        return instance
        

class SysUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = SysUser
        fields = ('username', 'phone', 'password')


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = "__all__"


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"