from authentication.models import User, Student_Profile, Faculty_Profile  # Importing models
from rest_framework import serializers  # Importing serializers from DRF
from typing import Dict, Any, Optional  # Import typing for type hints


class LoginSerializer(serializers.Serializer):
    """
    Serializer for handling user login requests.
    Validates required code and password fields.
    """
    # Define required fields with explicit types
    code: serializers.CharField = serializers.CharField(required=True)  # Code field (required)
    password: serializers.CharField = serializers.CharField(required=True)  # Password field (required)

    def validate(self, attrs: Dict[str, Any]) -> Dict[str, Any]:
        """
        Validates that both code and password are provided.
        
        Args:
            attrs: Dictionary containing serializer field values
            
        Returns:
            Dictionary of validated attributes
            
        Raises:
            ValidationError: If code or password is missing
        """
        # Extract user credentials from attributes
        code: Optional[str] = attrs.get('code')
        password: Optional[str] = attrs.get('password')

        # Validate that both required fields are provided
        if not code or not password:
            raise serializers.ValidationError("Code and password are required.")

        return attrs  # Return validated attributes


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for the User model.
    Handles secure password handling during create and update operations.
    """
    class Meta:
        model = User  # Link to User model
        fields = ['code', 'is_active', 'is_staff', 'password', 'is_superuser']  # Fields to include
        extra_kwargs = {
            'password': {'write_only': True},  # Password should be write-only
            'is_active': {'read_only': True},  # is_active is read-only
            'is_staff': {'read_only': True},  # is_staff is read-only
            'is_superuser': {'read_only': True},  # is_superuser is read-only
        }

    def create(self, validated_data: Dict[str, Any]) -> User:
        """
        Creates a new User instance with proper password hashing.
        
        Args:
            validated_data: Dictionary containing validated field values
            
        Returns:
            Newly created User instance
        """
        # Extract password separately for secure handling
        password: Optional[str] = validated_data.pop('password', None)
        
        # Create user instance with remaining data
        user: User = super().create(validated_data)

        # Set password securely if provided
        if password:
            user.set_password(password)  # Hash the password
            user.save()  # Save the updated user

        return user  # Return the created user

    def update(self, instance: User, validated_data: Dict[str, Any]) -> User:
        """
        Updates an existing User instance with proper password handling.
        
        Args:
            instance: Existing User instance to update
            validated_data: Dictionary containing validated field values
            
        Returns:
            Updated User instance
        """
        # Extract password separately for secure handling
        password: Optional[str] = validated_data.pop('password', None)
        
        # Update user instance with remaining data
        user: User = super().update(instance, validated_data)

        # Set password securely if provided
        if password:
            user.set_password(password)  # Hash the password
            user.save()  # Save the updated user

        return user  # Return the updated user


class Student_ProfileSerializer(serializers.ModelSerializer):
    """
    Serializer for the Student_Profile model.
    Handles creation and updates of student profile data.
    """
    class Meta:
        model = Student_Profile  # Link to Student_Profile model
        fields = '__all__'  # Include all fields
        extra_kwargs = {
            'user': {'read_only': False, 'required': False}  # Make user field optional
        }

    def create(self, validated_data: Dict[str, Any]) -> Student_Profile:
        """
        Creates a new Student_Profile instance.
        
        Args:
            validated_data: Dictionary containing validated field values
            
        Returns:
            Newly created Student_Profile instance
        """
        # Create and return a student profile instance
        return super().create(validated_data)

    def update(self, instance: Student_Profile, validated_data: Dict[str, Any]) -> Student_Profile:
        """
        Updates an existing Student_Profile instance.
        
        Args:
            instance: Existing Student_Profile instance to update
            validated_data: Dictionary containing validated field values
            
        Returns:
            Updated Student_Profile instance
        """
        # Update and return the student profile instance
        return super().update(instance, validated_data)


class Faculty_ProfileSerializer(serializers.ModelSerializer):
    """
    Serializer for the Faculty_Profile model.
    Handles creation and updates of faculty profile data.
    """
    class Meta:
        model = Faculty_Profile  # Link to Faculty_Profile model
        fields = '__all__'  # Include all fields
        extra_kwargs = {
            'user': {'read_only': False, 'required': False}  # Make user field optional
        }

    def create(self, validated_data: Dict[str, Any]) -> Faculty_Profile:
        """
        Creates a new Faculty_Profile instance.
        
        Args:
            validated_data: Dictionary containing validated field values
            
        Returns:
            Newly created Faculty_Profile instance
        """
        # Create and return a faculty profile instance
        return super().create(validated_data)

    def update(self, instance: Faculty_Profile, validated_data: Dict[str, Any]) -> Faculty_Profile:
        """
        Updates an existing Faculty_Profile instance.
        
        Args:
            instance: Existing Faculty_Profile instance to update
            validated_data: Dictionary containing validated field values
            
        Returns:
            Updated Faculty_Profile instance
        """
        # Update and return the faculty profile instance
        return super().update(instance, validated_data)
