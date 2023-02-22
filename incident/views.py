from django.shortcuts import render
from incident.models import *
from incident.serializers import *
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken

# Create your views here.

class SignUpUserView(APIView):
    '''This api is use for signup email,name,phone_number and password'''
    def post(self,requst):
        serializer = SignUpUserSerializers(data=requst.data)
        if serializer.is_valid():
            user = serializer.save()
            user.set_password(serializer.data['password'])
            user.save()
            return Response({
                'status':"success",
                'message':"account has been created successfully",
            },status=status.HTTP_201_CREATED)
        else:
            return Response({'status':serializer.errors})
        
class LoginUserView(APIView):
    '''This api is use for login with email and password'''
    def post(self,request):
        serializer = LoginUserSerializers(data=request.data)
        if serializer.is_valid(raise_exception=True):
            email = serializer.data.get("email")
            password = serializer.data.get("password")
            user = authenticate(email=email, password=password)

            if user is not None:
                refresh = RefreshToken.for_user(user)
                return Response({'status':"success",'refresh':str(refresh),"access":str(refresh.access_token),
                },status=status.HTTP_200_OK)

            else:
                return Response({'status':serializer.errors,"messages":"invalid credential"})

class GetAllUserView(APIView):
    permission_classes=(IsAuthenticated,)
    '''
        Get All Users
    '''
    def get(self,request):
        user = User.objects.all()
        serializer = UserSerializers(user, many=True)
        return Response(serializer.data)