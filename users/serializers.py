from rest_framework import serializers

from users.models import User

class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only = True)
    username = serializers.CharField(max_length=20)
    email = serializers.EmailField(max_length=127)
    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)
    birthdate = serializers.DateField()
    is_employee = serializers.BooleanField(default=False)
    is_superuser = serializers.BooleanField(default=False, read_only=True)

    def create(self, validated_data):


        if validated_data['is_employee'] == True:
            user = User.objects.create_superuser(**validated_data)

        else:
            user = User.objects.create_user(**validated_data)
        
        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
    is_superuser = serializers.BooleanField(read_only=True)