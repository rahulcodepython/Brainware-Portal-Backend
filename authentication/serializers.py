from authentication.models import User, Student_Profile, Faculty_Profile  # Importing models
from rest_framework import serializers  # Importing serializers from DRF


# Serializer for user login
class LoginSerializer(serializers.Serializer):
    code: str = serializers.CharField(required=True)  # Code field (required)
    password: str = serializers.CharField(
        required=True)  # Password field (required)

    def validate(self, attrs: dict) -> dict:
        # Extracting code and password from attributes
        code: str = attrs.get('code')
        password: str = attrs.get('password')

        # Validating that both fields are provided
        if not code or not password:
            raise serializers.ValidationError(
                "Code and password are required.")

        return attrs  # Returning validated attributes


# Serializer for user model
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User  # Linking to User model
        fields = ['code', 'is_active', 'is_staff',
                  'password', 'is_superuser']  # Fields to include
        extra_kwargs = {
            'password': {'write_only': True},  # Password should be write-only
            'is_active': {'read_only': True},  # is_active is read-only
            'is_staff': {'read_only': True},  # is_staff is read-only
            'is_superuser': {'read_only': True},  # is_superuser is read-only
        }

    def create(self, validated_data: dict) -> User:
        # Extracting password from validated data
        password: str = validated_data.pop('password', None)
        # Creating user instance
        user: User = super().create(validated_data)

        # Setting password if provided
        if password:
            user.set_password(password)
            user.save()

        return user  # Returning created user

    def update(self, instance: User, validated_data: dict) -> User:
        # Extracting password from validated data
        password: str = validated_data.pop('password', None)
        # Updating user instance
        user: User = super().update(instance, validated_data)

        # Setting password if provided
        if password:
            user.set_password(password)
            user.save()

        return user  # Returning updated user


# Serializer for student profile
class Student_ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student_Profile  # Linking to Student_Profile model
        fields = '__all__'  # Including all fields
        extra_kwargs = {
            # Making user field optional
            'user': {'read_only': False, 'required': False}
        }

    def create(self, validated_data: dict) -> Student_Profile:
        # Creating student profile instance
        return super().create(validated_data)

    def update(self, instance: Student_Profile, validated_data: dict) -> Student_Profile:
        # Updating student profile instance
        return super().update(instance, validated_data)


# Serializer for faculty profile
class Faculty_ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Faculty_Profile  # Linking to Faculty_Profile model
        fields = '__all__'  # Including all fields
        extra_kwargs = {
            # Making user field optional
            'user': {'read_only': False, 'required': False}
        }

    def create(self, validated_data: dict) -> Faculty_Profile:
        # Creating faculty profile instance
        return super().create(validated_data)

    def update(self, instance: Faculty_Profile, validated_data: dict) -> Faculty_Profile:
        # Updating faculty profile instance
        return super().update(instance, validated_data)
