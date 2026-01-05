from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.authentication import BasicAuthentication
from rest_framework.authtoken.models import Token
from rest_framework import status
from user_app.models import*
from user_app.serializers import*
from rest_framework.response import Response

# Create your views here.
class UserRegisteration(APIView):

    permission_classes = [AllowAny]

    def post(self,request):

        user_serializer = UserSerializer(data =request.data)

        if user_serializer.is_valid():

            user = user_serializer.save()

            return Response(user_serializer.data,status=status.HTTP_201_CREATED)
        
        return Response(user_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class LoginView(APIView):

    authentication_classes =[BasicAuthentication]
    
    permission_classes =[IsAuthenticated]


    def post(self,request):

        user = request.user

        token,created = Token.objects.get_or_create(user=user)

        return Response({"message":"login success","token":token.key},status=status.HTTP_200_OK)


    
