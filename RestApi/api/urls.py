from django.contrib import admin
from django.urls import path,include
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('',views.index,name="index"),
    path('login/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('add-emp',views.addemployee,name="add-emp"),
    path('get-emp',views.getemployee,name="get-emp"),
    path('update-emp/<str:pk>',views.updateemp,name="update-emp"),
    path('delete-emp/<str:pk>',views.deleteemployee,name="delete-emp"),
    path('Department',views.DepartmentApi.as_view(),name="Department"),
    path("Register",views.UserApi.as_view(),name="Register"),
    path("ImageTest",views.ImageTestApi.as_view(),name="ImageTest"),
  
]
