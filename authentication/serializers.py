from authentication.models import User, Student_Profile, Faculty_Profile
from rest_framework import serializers


class LoginSerializer(serializers.Serializer):
    code = serializers.CharField(required=True)
    password = serializers.CharField(required=True)

    def validate(self, attrs):
        code = attrs.get('code')
        password = attrs.get('password')

        if not code or not password:
            raise serializers.ValidationError(
                "Code and password are required.")

        return attrs


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['code', 'is_active',
                  'is_staff', 'password', 'is_superuser']
        extra_kwargs = {
            'password': {'write_only': True},
            'is_active': {'read_only': True},
            'is_staff': {'read_only': True},
            'is_superuser': {'read_only': True},
        }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        user = super().create(validated_data)

        if password:
            user.set_password(password)
            user.save()

        return user

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        user = super().update(instance, validated_data)

        if password:
            user.set_password(password)
            user.save()

        return user


class Student_ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student_Profile
        fields = '__all__'
        extra_kwargs = {
            'user': {'read_only': False, 'required': False}
        }

    def create(self, validated_data):
        return super().create(validated_data)

    def update(self, instance, validated_data):
        return super().update(instance, validated_data)


class Faculty_ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Faculty_Profile
        fields = '__all__'
        extra_kwargs = {
            'user': {'read_only': False, 'required': False}
        }

    def create(self, validated_data):
        return super().create(validated_data)

    def update(self, instance, validated_data):
        return super().update(instance, validated_data)
