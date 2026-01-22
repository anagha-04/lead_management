from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.authentication import BasicAuthentication,TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework import status
from user_app.models import*
from user_app.serializers import*
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken


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

        # jwt

        # refresh = RefreshToken.for_user(user) #usernmae password user_id
        
        # return Response(
        #     {
        #         "message":"login success",
        #         "access": str(refresh.access_token),
        #         "refresh": str(refresh)
        #     },
        #     status=status.HTTP_200_OK
        # )

        token,created = Token.objects.get_or_create(user=user)

        return Response({"message":"login success","token":token.key},status=status.HTTP_200_OK)

class StudentAddview(APIView):

    # authentication_classes=[TokenAuthentication]

    # permission_classes=[IsAuthenticated]

    def post(self,request):

        serializer = StudentLeadSerializer(data=request.data)

        if serializer.is_valid():

            serializer.save(user= request.user)

            return Response(serializer.data,status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors,status=status.HTTP_200_OK)
# list 
    def get(self,request):

        # data = StudentLeadModel.objects.filter(user= request.user)

        data = StudentLeadModel.objects.all()

        serializer = StudentLeadSerializer(data,many=True)

        return Response(serializer.data,status=status.HTTP_200_OK)
    
class StudentRetriveUpdateDeleteView(APIView):

    # authentication_classes = [TokenAuthentication]

    # permission_classes =[IsAuthenticated]

    def get(self,request,**kwargs):

        id = kwargs.get("pk")

        student = get_object_or_404(StudentLeadModel,id = id ,user = request.user)

        serializer = StudentLeadSerializer(student,many=False)
        
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def put(self,request,**kwargs):

        id = kwargs.get('pk')

        student = get_object_or_404(StudentLeadModel,id=id,user=request.user)

        serializer = StudentLeadSerializer(student,data=request.data)

        if serializer.is_valid():

            serializer.save()

            return Response(serializer.data,status=status.HTTP_200_OK)
        
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,**kwargs):

        id= kwargs.get('pk')

        student = get_object_or_404(StudentLeadModel,id=id)

        student.delete()

        return Response({"message":"service request deleted"},status=status.HTTP_200_OK)
    


    

    
