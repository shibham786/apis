
from rest_framework import serializers
from .models import Employee,Department,ImageTest
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        min_length = 8,
        required = True,
        error_messages = {
            "min_length":"password must be minimum 8 length"
        },
        style={'input_type': 'password', 'placeholder': ' Re-Password'}
    )

    password2 = serializers.CharField(
        write_only=True,
        min_length = 8,
        required = True,
        error_messages = {
            "min_length":"password must be minimum 8 length"
        },
        style={'input_type': 'password', 'placeholder': 'Password'}
    )

    class Meta:
        model = User
        fields = ['id','username','email','password','password2'] #yaha vahi field jo create k time dalna ho table m

    def validate(self, data):
        if data['password'] != data["password2"]:
            raise serializers.ValidationError("password must be same")
        return data
    def create(self, validated_data):
        user = User.objects.create(
            username = validated_data["username"],
            email = validated_data["email"],    
                  
        )

        user.set_password(validated_data["password"])
        user.save()

        return user


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"

class ImageTestSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageTest
        fields = "__all__"

   


class DepartmentSerializer(serializers.ModelSerializer):
    employees = serializers.SerializerMethodField()
    class Meta:
        model = Department
        fields = "__all__" 
    def get_employees(self,obj):
        employees = obj.employee_set.all()
        serializer = EmployeeSerializer(employees,many=True)
        return serializer.data
    
