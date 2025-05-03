from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView

from .models import Circle
from .serializers import UserSignupSerializer, CircleSerializer


class SignupView(generics.CreateAPIView):
    serializer_class = UserSignupSerializer
    permission_classes = [permissions.AllowAny]


class LoginView(TokenObtainPairView):
    permission_classes = [permissions.AllowAny]


class CreateCircleView(generics.CreateAPIView):
    serializer_class = CircleSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        circle = serializer.save()
        circle.members.add(self.request.user)


class JoinCircleView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, code):
        try:
            circle = Circle.objects.get(invite_code=code)
        except Circle.DoesNotExist:
            return Response({"detail": "Circle not found"}, status=status.HTTP_404_NOT_FOUND)
        circle.members.add(request.user)
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
