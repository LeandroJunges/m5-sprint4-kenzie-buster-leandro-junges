from rest_framework.views import APIView, Request, Response,status

from users.permissions import IsUserOrAdm
from  .serializers import LoginSerializer, UserSerializer
from .models import User
from rest_framework_simplejwt.views import TokenObtainPairView
import ipdb
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication




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

class UserDetail(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsUserOrAdm]

    
    def get(self, request: Request, user_id)-> Response:

        user = get_object_or_404(User, pk=user_id)
        self.check_object_permissions(request ,user)



        serializer = UserSerializer(user)

        return Response(serializer.data, status=status.HTTP_200_OK)




class LoginView(TokenObtainPairView):
    ...