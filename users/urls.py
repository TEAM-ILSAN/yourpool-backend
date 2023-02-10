# from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.urls import path
from .views import SignupView, updategeo


urlpatterns = [
    path("signup/", SignupView.as_view(), name="signup"),
    # path("login/", RegistrationAPIView.as_view(), name="register"),
    path('updategeo/', updategeo),
]
