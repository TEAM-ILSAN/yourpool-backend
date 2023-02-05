from django.urls import path
from .views import SignupView, VerifyOTP, LoginView


urlpatterns = [
    path("signup/", SignupView.as_view(), name="signup"),
    path("login/", LoginView.as_view(), name="login"),
    path("verify/", VerifyOTP.as_view(), name="verity-otp"),
]
