from django.urls import path
from .views import SignupView, VerifyOTP


urlpatterns = [
    path("signup/", SignupView.as_view(), name="signup"),
    path("verify/", VerifyOTP.as_view(), name="verity-otp"),
]
