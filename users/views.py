from rest_framework.views import APIView, Request, Response,status
from  .serializers import LoginSerializer, UserSerializer
from .models import User
from django.contrib.auth import authenticate
from rest_framework_simplejwt.views import TokenObtainPairView


class RegisterUser(APIView):
    
    def get(self, request: Request)-> Response:

        user = User.objects.all()
        serializer = UserSerializer(user, many=True)        

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request: Request)-> Response:

        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

class LoginView(TokenObtainPairView):
   ...