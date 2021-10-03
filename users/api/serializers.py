
from rest_framework import serializers
from django.contrib.auth.models import User

from users.models import Student


class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'},write_only =True)


    class Meta:
        model = User
        fields = ['email','first_name','last_name','username','password','password2']
        # extra_kwargs = {
        #     'password': {'write_only':True}
        # }

    def save(self):
        user = User(email=self.validated_data['email'],
                          username=self.validated_data['username'])

        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        if password == password2:
            user.set_password(password)
            user.save()

            return user
        else:
            raise serializers.ValidationError({'password': "Passwords do not match"})

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['course','study_level','image_url','department']
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

