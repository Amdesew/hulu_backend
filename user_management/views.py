from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
#from django.contrib.auth.decorators import login_required

class RegisterUser(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data['username']
        password = request.data['password']
        user = User.objects.create_user(username=username, password=password)
        return Response({'message': 'User registered'}, status=status.HTTP_201_CREATED)

class LogoutUser(APIView):
    def post(self, request):
        token = RefreshToken(request.data['refresh'])
        token.blacklist()
        return Response({'message': 'User logged out'}, status=status.HTTP_205_RESET_CONTENT)

class ProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        return Response({"username": user.username, "email": user.email})


class user_details(APIView):    
    
    def get(self, request):
        user = request.user
        return Response({
            'id': user.id,
            'username': user.username,
        })
