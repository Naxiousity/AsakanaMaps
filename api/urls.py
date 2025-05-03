"""
URL configuration for asakana project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from .views import SignupView, LoginView, CreateCircleView, JoinCircleView, LocationUpdateView, LatestLocationsView

urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('circles/', CreateCircleView.as_view(), name='create_circle'),
    path('circles/join/<str:code>/', JoinCircleView.as_view(), name='join_circle'),
    path('locations/update/', LocationUpdateView.as_view(), name='location_update'),
    path('locations/latest/', LatestLocationsView.as_view(), name='latest_locations'),
]