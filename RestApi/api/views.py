from django.shortcuts import render
from django.http import Http404, HttpResponse
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import Department, Employee,ImageTest
from .serializers import EmployeeSerializer,DepartmentSerializer, ImageTestSerializer,UserSerializer
from rest_framework import serializers,viewsets,generics
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User




# Create your views here.

def index(request):
    return render(request,'index.html')

@api_view(['POST'])
@permission_classes([IsAuthenticated]) #for authentication
def addemployee(request):
    # print(request.user)
   
    emp = EmployeeSerializer(data=request.data)
    if Employee.objects.filter(**request.data).exists():
        raise serializers.ValidationError("Record Already exists")
    if emp.is_valid():
        emp.save()
        return Response(emp.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getemployee(request):
   qs = Employee.objects.all()
   serializer = EmployeeSerializer(qs,many=True)
   return Response(serializer.data)

@api_view(['POST'])
def updateemp(request,pk):
   qs = Employee.objects.get(id=pk)
   emp = EmployeeSerializer(instance=qs,data=request.data)
   if emp.is_valid():
       emp.save()
       return Response(emp.data)
   else:
        return  serializers.ValidationError("Not Found")

@api_view(['GET'])
def deleteemployee(request,pk):
   qs = Employee.objects.get(id=pk)
   qs.delete()
   return Response("Record Deleted")


#class based views example

class DepartmentApi(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request):
        qs = Department.objects.all()
        serializer = DepartmentSerializer(qs,many=True)
        return Response({'status':200,'payload':serializer.data})

    
    def post(self,request):
         dept = DepartmentSerializer(data=request.data)
         if  Department.objects.filter(**request.data).exists():
               raise serializers.ValidationError({'status':400,'message':'Record already Exists'})

         if dept.is_valid():
            dept.save()
            return Response(dept.data)
    
    def put(self,request):
        pass
    
    def delete(self,request):
        pass


class UserApi(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


#class based views example

class ImageTestApi(APIView):

    def get(self,request):
        qs = ImageTest.objects.all()
        serializer = ImageTestSerializer(qs,many=True)
        return Response({'status':200,'payload':serializer.data})

    
    def post(self,request):
         img = ImageTestSerializer(data=request.data)
         if  ImageTest.objects.filter(**request.data).exists():
               raise serializers.ValidationError({'status':400,'message':'Record already Exists'})

         if img.is_valid():
            img.save()
            return Response(img.data)
    
   

