from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView

from .models import Circle, LocationUpdate
from .serializers import UserSignupSerializer, CircleSerializer, LocationUpdateSerializer


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
    
    
class LocationUpdateView(generics.CreateAPIView):
    """POST /api/auth/locations/update/"""
    serializer_class = LocationUpdateSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class LatestLocationsView(generics.ListAPIView):
    """GET /api/auth/locations/latest/"""
    serializer_class = LocationUpdateSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        circles = user.circles.all()
        members = set(u for c in circles for u in c.members.all())

        queryset = (
            LocationUpdate.objects
            .filter(user_in=members)
            .order_by('user', '-timestamp')
            .distinct('user')
        )
        
        return queryset